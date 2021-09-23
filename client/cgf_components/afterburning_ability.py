# Embedded file name: scripts/client/cgf_components/afterburning_ability.py
import CGF
import GenericComponents
from cgf_script.component_meta_class import CGFComponent, ComponentProperty, CGFMetaTypes
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery, Rule, registerManager
from CustomEffectManager import CustomEffectManager

class CustomEffectsModifier(CGFComponent):
    value = ComponentProperty(type=CGFMetaTypes.INT, editorName='Value', value=0)
    key = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Key', value='')


class CustomEffectsModifierManager(CGF.ComponentManager):

    @onAddedQuery(CustomEffectsModifier, GenericComponents.RedirectorComponent)
    def onAdded(self, modifier, redirector):
        effectMgr = redirector.redirectionTarget.findComponentByType(CustomEffectManager)
        if effectMgr is not None:
            effectMgr.variables[modifier.key] = modifier.value
        return

    @onRemovedQuery(CustomEffectsModifier, GenericComponents.RedirectorComponent)
    def onRemoved(self, modifier, redirector):
        effectMgr = redirector.redirectionTarget.findComponentByType(CustomEffectManager)
        if effectMgr is not None:
            effectMgr.variables[modifier.key] = 0
        return


class AfterburningRule(Rule):

    @registerManager(CustomEffectsModifierManager)
    def reg(self):
        return None