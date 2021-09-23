# Embedded file name: scripts/client/gui/Scaleform/locale/EVENT.py
from debug_utils import LOG_WARNING

class EVENT(object):
    PUNISHMENTWINDOW_REASON_EVENT_DESERTER = '#event:punishmentWindow/reason/event_deserter'
    PUNISHMENTWINDOW_REASON_EVENT_AFK = '#event:punishmentWindow/reason/event_afk'
    BATTLEHINTS_TESTMESSAGE = '#event:battleHints/testMessage'
    BATTLEHINTS_TESTMESSAGEWITHPARAMS = '#event:battleHints/testMessageWithParams'
    CRAFTMACHINE_TITLE = '#event:craftMachine/title'
    CRAFTMACHINE_SUBTITLE = '#event:craftMachine/subTitle'
    CRAFTMACHINE_STATUSDATE = '#event:craftMachine/statusDate'
    MENU_SELECTOR_TITLE = '#event:menu/selector/title'
    MENU_SELECTOR_UNAVAILABLE = '#event:menu/selector/unavailable'
    TOOLTIPS_SELECTOR_TITLE = '#event:tooltips/selector/title'
    TOOLTIPS_SELECTOR_DESC = '#event:tooltips/selector/desc'
    TOOLTIPS_SELECTOR_TIMETABLE_TITLE = '#event:tooltips/selector/timeTable/title'
    TOOLTIPS_SELECTOR_TIMETABLE_TODAY = '#event:tooltips/selector/timeTable/today'
    TOOLTIPS_SELECTOR_TIMETABLE_TOMORROW = '#event:tooltips/selector/timeTable/tomorrow'
    TOOLTIPS_SELECTOR_TIMETABLE_EMPTY = '#event:tooltips/selector/timeTable/empty'
    TOOLTIPS_SELECTOR_TIMETABLE_TILLEND = '#event:tooltips/selector/timeTable/tillEnd'
    SELECTORTOOLTIP_TIMETABLE_TITLE = '#event:selectorTooltip/timeTable/title'
    SELECTORTOOLTIP_TIMETABLE_TILLEND = '#event:selectorTooltip/timeTable/tillEnd'
    QUESTS_ERROR_NO_TICKET = '#event:quests/error/no_ticket'
    QUESTS_ERROR_NO_TICKET_TOOLTIP_HEADER = '#event:quests/error/no_ticket/tooltip/header'
    QUESTS_ERROR_NO_TICKET_TOOLTIP_BODY = '#event:quests/error/no_ticket/tooltip/body'
    TOOLTIPS_HEADER_QUESTS_HEADER_EVENT_HUNTER = '#event:tooltips/header/quests/header/event_hunter'
    TOOLTIPS_HEADER_QUESTS_HEADER_EVENT_BOSS = '#event:tooltips/header/quests/header/event_boss'
    TOOLTIPS_HEADER_QUESTS_HEADER_DESCRIPTION_TILL_END = '#event:tooltips/header/quests/header/description/till_end'
    TOOLTIPS_HEADER_QUESTS_HEADER_DESCRIPTION_TILL_UPD = '#event:tooltips/header/quests/header/description/till_upd'
    TOOLTIPS_HEADER_QUESTS_HEADER_UNAVAILABLE = '#event:tooltips/header/quests/header/unavailable'
    TOOLTIPS_HEADER_QUESTS_HEADER_DESCRIPTION_UNAVAILABLE = '#event:tooltips/header/quests/header/description/unavailable'
    TOOLTIPS_HEADER_QUESTS_HEADER_SPECIAL_EVENT_BOSS = '#event:tooltips/header/quests/header/special_event_boss'
    TOOLTIPS_HEADER_QUESTS_BOTTOM = '#event:tooltips/header/quests/bottom'
    CALENDARDAY_TITLE = '#event:calendarDay/title'
    CALENDARDAY_SERVERNAME = '#event:calendarDay/serverName'
    CALENDARDAY_TIME = '#event:calendarDay/time'
    STATUS_TIMELEFT_DAYS = '#event:status/timeLeft/days'
    STATUS_TIMELEFT_HOURS = '#event:status/timeLeft/hours'
    STATUS_TIMELEFT_LESSHOUR = '#event:status/timeLeft/lessHour'
    STATUS_TIMELEFT_MIN = '#event:status/timeLeft/min'
    STATUS_TIMELEFT_LESSMIN = '#event:status/timeLeft/lessMin'
    STATUS_UNAVAILABLE = '#event:status/unavailable'
    WTEVENTSENTRYPOINT_TITLE = '#event:WTEventsEntryPoint/title'
    WTEVENTSENTRYPOINT_ACTIVE = '#event:WTEventsEntryPoint/active'
    WTEVENTSENTRYPOINT_FROZEN = '#event:WTEventsEntryPoint/frozen'
    WTEVENTAWARDSVIEW_MAINREWARDS_BUTTON = '#event:WTEventAwardsView/mainRewards/button'
    WTEVENTAWARDSVIEW_MAINREWARDS_BACK_PORTAL = '#event:WTEventAwardsView/mainRewards/back_portal'
    WTEVENTAWARDSVIEW_MAINREWARDS_PREMIUM_PLUS = '#event:WTEventAwardsView/mainRewards/premium_plus'
    WTEVENTAWARDSVIEW_MAINREWARDS_WT_BOSS = '#event:WTEventAwardsView/mainRewards/wt_boss'
    WTEVENTAWARDSVIEW_DESCIPTION = '#event:WTEventAwardsView/desciption'
    WTEVENTAWARDSVIEW_TITLE = '#event:WTEventAwardsView/title'
    WTEVENTAWARDSVIEW_STATUS_PART = '#event:WTEventAwardsView/status/part'
    WTEVENTAWARDSVIEW_STATUS_ALL = '#event:WTEventAwardsView/status/all'
    WTEVENTAWARDSVIEW_STATUS_POSTBATTLE = '#event:WTEventAwardsView/status/postBattle'
    WINDOW_UNIT_MESSAGE_VEHICLENOTSELECTED = '#event:window/unit/message/vehicleNotSelected'
    SIMPLESQUAD_SELECTRESTRICTION = '#event:simpleSquad/selectRestriction'
    WTEVENTWELCOMEVIEW_WELCOME_TITLE = '#event:WTEventWelcomeView/welcome/title'
    WTEVENTWELCOMEVIEW_WELCOME_COLLECTION_TITLE = '#event:WTEventWelcomeView/welcome/collection_title'
    WTEVENTWELCOMEVIEW_WELCOME_COLLECTION_TEXT = '#event:WTEventWelcomeView/welcome/collection_text'
    WTEVENTWELCOMEVIEW_WELCOME_ASYMMETRY_TITLE = '#event:WTEventWelcomeView/welcome/asymmetry_title'
    WTEVENTWELCOMEVIEW_WELCOME_ASYMMETRY_TEXT = '#event:WTEventWelcomeView/welcome/asymmetry_text'
    WTEVENTWELCOMEVIEW_WELCOME_WT_WELCOME_TITLE = '#event:WTEventWelcomeView/welcome/wt_welcome_title'
    WTEVENTWELCOMEVIEW_WELCOME_WT_WELCOME_TEXT = '#event:WTEventWelcomeView/welcome/wt_welcome_text'
    WTEVENTWELCOMEVIEW_WELCOME_CONFIRM_BTN = '#event:WTEventWelcomeView/welcome/confirm_btn'
    WTEVENTAMMUNITIONTOOLTIPVIEW_ADDITIONALINFOTITLE = '#event:WtEventAmmunitionTooltipView/additionalInfoTitle'
    WTEVENTLOOTBOXESINFOVIEW_TOOLTIP_TITLE = '#event:WtEventLootBoxesInfoView/tooltip/title'
    WTEVENTLOOTBOXESINFOVIEW_TOOLTIP_HUNTERSUBTITLE = '#event:WtEventLootBoxesInfoView/tooltip/hunterSubtitle'
    WTEVENTLOOTBOXESINFOVIEW_TOOLTIP_HUNTERTEXT = '#event:WtEventLootBoxesInfoView/tooltip/hunterText'
    WTEVENTLOOTBOXESINFOVIEW_TOOLTIP_BOSSSUBTITLE = '#event:WtEventLootBoxesInfoView/tooltip/bossSubtitle'
    WTEVENTLOOTBOXESINFOVIEW_TOOLTIP_BOSSTEXT = '#event:WtEventLootBoxesInfoView/tooltip/bossText'
    WTEVENTSCAROUSELVIEW_INBATTLETEXT = '#event:WTEventsCarouselView/inBattleText'
    WTEVENTSCAROUSELVIEW_INPLATOONTEXT = '#event:WTEventsCarouselView/inPlatoonText'
    WTEVENTSCAROUSELVIEW_UNSUITABLETEXT = '#event:WTEventsCarouselView/unsuitableText'
    WTEVENTSCAROUSELVIEW_TICKETNEEDEDTEXT = '#event:WTEventsCarouselView/ticketNeededText'
    WTEVENTSTICKETMESSAGEVIEW_BOSS_DESCRIPTION = '#event:WTEventsTicketMessageView/boss/description'
    WTEVENTSTICKETMESSAGEVIEW_BUYTEXT = '#event:WTEventsTicketMessageView/buyText'
    WTEVENTSTICKETMESSAGEVIEW_TASKTEXT = '#event:WTEventsTicketMessageView/taskText'
    WTEVENTPORTALS_MAINTITLE = '#event:WtEventPortals/mainTitle'
    WTEVENTPORTALS_WARNING = '#event:WtEventPortals/warning'
    WTEVENTPORTALS_PRICE = '#event:WtEventPortals/price'
    WTEVENTPORTALS_BUYBUTTON = '#event:WtEventPortals/buyButton'
    WTEVENTPORTALS_BUYBUTTONCNTEXT = '#event:WtEventPortals/buyButtonCNText'
    WTEVENTPORTALS_BUYBUTTONTOOLTIP = '#event:WtEventPortals/buyButtonTooltip'
    WTEVENTPORTALS_TITLE_HUNTER = '#event:WtEventPortals/title/hunter'
    WTEVENTPORTALS_TEXT_HUNTER = '#event:WtEventPortals/text/hunter'
    WTEVENTPORTALS_SUBTITLE_HUNTER = '#event:WtEventPortals/subtitle/hunter'
    WTEVENTPORTALS_DESCRIPTION_HUNTER = '#event:WtEventPortals/description/hunter'
    WTEVENTPORTALS_TITLE_BOSS = '#event:WtEventPortals/title/boss'
    WTEVENTPORTALS_TEXT_BOSS = '#event:WtEventPortals/text/boss'
    WTEVENTPORTALS_BOSS_LEFT = '#event:WtEventPortals/boss/left'
    WTEVENTPORTALS_BOSS_ONELEFT = '#event:WtEventPortals/boss/oneLeft'
    WTEVENTPORTALS_TITLE_TANK = '#event:WtEventPortals/title/tank'
    WTEVENTPORTALS_TEXT_TANK = '#event:WtEventPortals/text/tank'
    WTEVENTPORTALS_TANKINHANGAR = '#event:WtEventPortals/tankInHangar'
    WTEVENTPORTALS_SUBTITLE_BOSS = '#event:WtEventPortals/subtitle/boss'
    WTEVENTPORTALS_DESCRIPTION_BOSS = '#event:WtEventPortals/description/boss'
    WTEVENTPORTALS_INSIDE_BACKBUTTON = '#event:WtEventPortals/inside/backButton'
    WTEVENTPORTALS_INSIDE_SUBTITLE = '#event:WtEventPortals/inside/subtitle'
    WTEVENTPORTALS_INSIDE_NUMBERING = '#event:WtEventPortals/inside/numbering'
    WTEVENTPORTALS_INSIDE_HIGHPROBABILITY = '#event:WtEventPortals/inside/highProbability'
    WTEVENTPORTALS_INSIDE_GUARANTEEDPROBABILITY = '#event:WtEventPortals/inside/guaranteedProbability'
    WTEVENTPORTALS_INSIDE_MEDIUMPROBABILITY = '#event:WtEventPortals/inside/mediumProbability'
    WTEVENTPORTALS_INSIDE_LOWPROBABILITY = '#event:WtEventPortals/inside/lowProbability'
    WTEVENTPORTALS_INSIDE_LOWPROBABILITYTANK = '#event:WtEventPortals/inside/lowProbabilityTank'
    WTEVENTPORTALS_INSIDE_SHOWANIMATION = '#event:WtEventPortals/inside/showAnimation'
    WTEVENTPORTALS_INSIDE_TIMES = '#event:WtEventPortals/inside/times'
    WTEVENTPORTALS_INSIDE_PLURALTIMES = '#event:WtEventPortals/inside/pluralTimes'
    WTEVENTPORTALS_INSIDE_BUTTONRUNPORTAL = '#event:WtEventPortals/inside/buttonRunPortal'
    WTEVENTPORTALS_INSIDE_BUTTONTAKETANK = '#event:WtEventPortals/inside/buttonTakeTank'
    WTEVENTPORTALS_INSIDE_CURRENTKEYSAMOUNT_HUNTER = '#event:WtEventPortals/inside/currentKeysAmount/hunter'
    WTEVENTPORTALS_INSIDE_CURRENTKEYSAMOUNT_BOSS = '#event:WtEventPortals/inside/currentKeysAmount/boss'
    WTEVENTPORTALS_INSIDE_CURRENTKEYSAMOUNTIS0_HUNTER = '#event:WtEventPortals/inside/currentKeysAmountIs0/hunter'
    WTEVENTPORTALS_INSIDE_CURRENTKEYSAMOUNTIS0_BOSS = '#event:WtEventPortals/inside/currentKeysAmountIs0/boss'
    WTEVENTPORTALS_INSIDE_REWARDS_HUNTERCOLLECTIONELEMENT = '#event:WtEventPortals/inside/rewards/hunterCollectionElement'
    WTEVENTPORTALS_INSIDE_REWARDS_BOSSKEY = '#event:WtEventPortals/inside/rewards/bossKey'
    WTEVENTPORTALS_INSIDE_REWARDS_STYLE3D = '#event:WtEventPortals/inside/rewards/style3d'
    WTEVENTPORTALS_INSIDE_REWARDS_TANK = '#event:WtEventPortals/inside/rewards/tank'
    WTEVENTPORTALS_INSIDE_REWARDS_TANKS = '#event:WtEventPortals/inside/rewards/tanks'
    WTEVENTPORTALS_INSIDE_REWARDS_TANKSSEPARATOR = '#event:WtEventPortals/inside/rewards/tanksSeparator'
    WTEVENTPORTALS_INSIDE_REWARDS_TANKSTOOLTIP_HEADER = '#event:WtEventPortals/inside/rewards/tanksTooltip/header'
    WTEVENTPORTALS_INSIDE_REWARDS_TANKSTOOLTIP_BODY = '#event:WtEventPortals/inside/rewards/tanksTooltip/body'
    WTEVENTPORTALS_INSIDE_REWARDS_TANKDESCRIPTION = '#event:WtEventPortals/inside/rewards/tankDescription'
    WTGUARANTEEDREWARDTOOLTIPVIEW_TITLE = '#event:WtGuaranteedRewardTooltipView/title'
    WTGUARANTEEDREWARDTOOLTIPVIEW_PORTALRUNS = '#event:WtGuaranteedRewardTooltipView/portalRuns'
    WTGUARANTEEDREWARDTOOLTIPVIEW_DESCRIPTION = '#event:WtGuaranteedRewardTooltipView/description'
    WTGUARANTEEDREWARDTOOLTIPVIEW_PORTALRUNSLEFT = '#event:WtGuaranteedRewardTooltipView/portalRunsLeft'
    WTGUARANTEEDREWARDTOOLTIPVIEW_VEHICLESTITLE = '#event:WtGuaranteedRewardTooltipView/vehiclesTitle'
    WTGUARANTEEDREWARDTOOLTIPVIEW_VEHICLESDESCRIPTION = '#event:WtGuaranteedRewardTooltipView/vehiclesDescription'
    WTEVENTPORTALS_COLLECTIONTOOLTIP_HUNTERCOLLECTION_TITLE = '#event:WtEventPortals/collectionTooltip/hunterCollection/title'
    WTEVENTPORTALS_COLLECTIONTOOLTIP_HUNTERCOLLECTION_DESCRIPTION = '#event:WtEventPortals/collectionTooltip/hunterCollection/description'
    WTEVENTPORTALS_COLLECTIONTOOLTIP_HUNTERCOLLECTION_STATUS_NOTCOLLECTED = '#event:WtEventPortals/collectionTooltip/hunterCollection/status/notCollected'
    WTEVENTPORTALS_COLLECTIONTOOLTIP_HUNTERCOLLECTION_STATUS_COLLECTED = '#event:WtEventPortals/collectionTooltip/hunterCollection/status/collected'
    WTEVENTPORTALS_COLLECTIONTOOLTIP_RANDOMSTYLE2D_TITLE = '#event:WtEventPortals/collectionTooltip/randomStyle2d/title'
    WTEVENTPORTALS_COLLECTIONTOOLTIP_RANDOMSTYLE2D_DESCRIPTION = '#event:WtEventPortals/collectionTooltip/randomStyle2d/description'
    WTEVENTPORTALS_COLLECTIONTOOLTIP_RANDOMDECAL_TITLE = '#event:WtEventPortals/collectionTooltip/randomDecal/title'
    WTEVENTPORTALS_COLLECTIONTOOLTIP_RANDOMDECAL_DESCRIPTION = '#event:WtEventPortals/collectionTooltip/randomDecal/description'
    WTEVENTPORTALS_COLLECTIONTOOLTIP_RANDOMSTYLE3D_TITLE = '#event:WtEventPortals/collectionTooltip/randomStyle3d/title'
    WTEVENTPORTALS_COLLECTIONTOOLTIP_RANDOMSTYLE3D_DESCRIPTION = '#event:WtEventPortals/collectionTooltip/randomStyle3d/description'
    WTEVENTPORTALS_COLLECTIONTOOLTIP_RANDOMSTYLE3D_STATUS_NOTCOLLECTED = '#event:WtEventPortals/collectionTooltip/randomStyle3d/status/notCollected'
    WTEVENTPORTALS_COLLECTIONTOOLTIP_RANDOMSTYLE3D_STATUS_COLLECTED = '#event:WtEventPortals/collectionTooltip/randomStyle3d/status/collected'
    WTEVENTBUYLOOTBOXESTOOLTIPVIEW_TITLE = '#event:WtEventBuyLootBoxesTooltipView/title'
    WTEVENTBUYLOOTBOXESTOOLTIPVIEW_DESCRIPTION = '#event:WtEventBuyLootBoxesTooltipView/description'
    WTEVENTBUYLOOTBOXESTOOLTIPVIEW_AMOUNTLEFT = '#event:WtEventBuyLootBoxesTooltipView/amountLeft'
    WTEVENTBUYLOOTBOXESTOOLTIPVIEW_INFO = '#event:WtEventBuyLootBoxesTooltipView/info'
    WTEVENTBUYLOOTBOXESTOOLTIPVIEW_ADDITIONALINFO = '#event:WtEventBuyLootBoxesTooltipView/additionalInfo'
    BONUSTOOLTIP_GOLD_HEADER = '#event:bonusTooltip/gold/header'
    BONUSTOOLTIP_GOLD_BODY = '#event:bonusTooltip/gold/body'
    BONUSTOOLTIP_CREWBOOKS_HEADER = '#event:bonusTooltip/crewBooks/header'
    BONUSTOOLTIP_CREWBOOKS_BODY = '#event:bonusTooltip/crewBooks/body'
    BONUSTOOLTIP_BOOSTER_CREDITS_HEADER = '#event:bonusTooltip/booster_credits/header'
    BONUSTOOLTIP_BOOSTER_CREDITS_BODY = '#event:bonusTooltip/booster_credits/body'
    BONUSTOOLTIP_BOOSTER_CREW_XP_HEADER = '#event:bonusTooltip/booster_crew_xp/header'
    BONUSTOOLTIP_BOOSTER_CREW_XP_BODY = '#event:bonusTooltip/booster_crew_xp/body'
    BONUSTOOLTIP_BOOSTER_FREE_XP_HEADER = '#event:bonusTooltip/booster_free_xp/header'
    BONUSTOOLTIP_BOOSTER_FREE_XP_BODY = '#event:bonusTooltip/booster_free_xp/body'
    BONUSTOOLTIP_BOOSTER_XP_HEADER = '#event:bonusTooltip/booster_xp/header'
    BONUSTOOLTIP_BOOSTER_XP_BODY = '#event:bonusTooltip/booster_xp/body'
    ELEMENTBONUS_DESC_STYLE3D = '#event:elementBonus/desc/style3d'
    BONUSNAME_SLOTS = '#event:bonusName/slots'
    COLLECTION_TITLE = '#event:collection/title'
    COLLECTION_ABOUT = '#event:collection/about'
    COLLECTION_COLLECTED = '#event:collection/collected'
    COLLECTION_COLLECTEDALL = '#event:collection/collectedAll'
    TOOLTIPS_TITLE = '#event:tooltips/title'
    TOOLTIPS_SUBTITLE = '#event:tooltips/subtitle'
    TOOLTIPS_PROGRESS_TEXT = '#event:tooltips/progress_text'
    TOOLTIPS_COMPLETE_TEXT = '#event:tooltips/complete_text'
    TOOLTIPS_FOOTER_FIRST_COLECTION = '#event:tooltips/footer/first_colection'
    TOOLTIPS_FOOTER_SECOND_COLECTION = '#event:tooltips/footer/second_colection'
    COLLECTIONTOOLTIP_TITLE_HUNTER = '#event:collectionTooltip/title/hunter'
    COLLECTIONTOOLTIP_TITLEFINAL_HUNTER = '#event:collectionTooltip/titleFinal/hunter'
    COLLECTIONTOOLTIP_DESCRIPTION_HUNTER = '#event:collectionTooltip/description/hunter'
    COLLECTIONTOOLTIP_FINALDESCRIPTION_HUNTER = '#event:collectionTooltip/finalDescription/hunter'
    COLLECTIONTOOLTIP_TITLE_BOSS = '#event:collectionTooltip/title/boss'
    COLLECTIONTOOLTIP_TITLEFINAL_BOSS = '#event:collectionTooltip/titleFinal/boss'
    COLLECTIONTOOLTIP_DESCRIPTION_BOSS = '#event:collectionTooltip/description/boss'
    COLLECTIONTOOLTIP_FINALDESCRIPTION_BOSS = '#event:collectionTooltip/finalDescription/boss'
    BATTLEQUEUE_WIDGET_BTNLABEL = '#event:battleQueue/widget/btnLabel'
    BATTLEQUEUE_WIDGET_CALCULATEDTEXT = '#event:battleQueue/widget/calculatedText'
    BATTLEQUEUE_WIDGET_CHANGETITLE = '#event:battleQueue/widget/changeTitle'
    BATTLEQUEUE_WIDGET_OFFERHUNTERTTILE = '#event:battleQueue/widget/offerHunterTtile'
    BATTLEQUEUE_WIDGET_TICKETTEXT = '#event:battleQueue/widget/ticketText'
    BATTLEQUEUE_WIDGET_BONUS = '#event:battleQueue/widget/bonus'
    BATTLEQUEUE_AVGWAITTIME_LABEL = '#event:battleQueue/avgWaitTime/label'
    BATTLEQUEUE_WIDGET_BONUSDESCR = '#event:battleQueue/widget/bonusDescr'
    VEHICLE_TAGS_EVENT_BOSS_NAME = '#event:vehicle/tags/event_boss/name'
    VEHICLE_TAGS_EVENT_HUNTER_NAME = '#event:vehicle/tags/event_hunter/name'
    PRIMETIME_TITLE = '#event:primeTime/title'
    PRIMETIME_STATUS_ALLSERVERSDISABLED = '#event:primeTime/status/allServersDisabled'
    PRIMETIME_STATUS_UNTILL = '#event:primeTime/status/untill'
    PRIMETIME_STATUS_DISABLEFIRST = '#event:primeTime/status/disableFirst'
    PRIMETIME_ENDOFCYCLE = '#event:primeTime/endOfCycle'
    PRIMETIME_STATUS_PRIMEISAVAILABLE = '#event:primeTime/status/primeIsAvailable'
    PRIMETIME_STATUS_PRIMEWILLBEAVAILABLE = '#event:primeTime/status/primeWillBeAvailable'
    PRIMETIME_SERVERTOOLTIP = '#event:primeTime/serverTooltip'
    PRIMETIME_SERVERUNAVAILABLETOOLTIP = '#event:primeTime/serverUnavailableTooltip'
    SERVERALERTMESSAGE = '#event:serverAlertMessage'
    SERVERALERTMESSAGE_BUTTON = '#event:serverAlertMessage/button'
    CREWPANEL_ROLE_BOSS = '#event:crewPanel/role/boss'
    CREWPANEL_SLOGAN_BOSS = '#event:crewPanel/slogan/boss'
    CREWPANEL_ROLE_HUNTER_1 = '#event:crewPanel/role/hunter_1'
    CREWPANEL_SLOGAN_HUNTER_1 = '#event:crewPanel/slogan/hunter_1'
    CREWPANEL_ROLE_HUNTER_2 = '#event:crewPanel/role/hunter_2'
    CREWPANEL_SLOGAN_HUNTER_2 = '#event:crewPanel/slogan/hunter_2'
    CREWPANEL_ROLE_HUNTER_3 = '#event:crewPanel/role/hunter_3'
    CREWPANEL_SLOGAN_HUNTER_3 = '#event:crewPanel/slogan/hunter_3'
    TANKMANTOOLTIP_STATUS_BOSS = '#event:tankmanTooltip/status/boss'
    TANKMANTOOLTIP_STATUS_HUNTER = '#event:tankmanTooltip/status/hunter'
    TANKMANTOOLTIP_BOSS_DESCR = '#event:tankmanTooltip/boss/descr'
    TANKMANTOOLTIP_HUNTER_1_DESCR = '#event:tankmanTooltip/hunter_1/descr'
    TANKMANTOOLTIP_HUNTER_2_DESCR = '#event:tankmanTooltip/hunter_2/descr'
    TANKMANTOOLTIP_HUNTER_3_DESCR = '#event:tankmanTooltip/hunter_3/descr'
    TANKMANTOOLTIP_SKILLSTITLE = '#event:tankmanTooltip/skillsTitle'
    BONUSES_HUNTER_COLLECTION_TOOLTIP_HEADER = '#event:bonuses/hunter_collection/tooltip/header'
    BONUSES_HUNTER_COLLECTION_TOOLTIP_BODY = '#event:bonuses/hunter_collection/tooltip/body'
    BONUSES_BOSS_COLLECTION_TOOLTIP_HEADER = '#event:bonuses/boss_collection/tooltip/header'
    BONUSES_BOSS_COLLECTION_TOOLTIP_BODY = '#event:bonuses/boss_collection/tooltip/body'
    LOADING_HUNTER_HEADER_1 = '#event:loading/hunter/header/1'
    LOADING_HUNTER_HEADER_2 = '#event:loading/hunter/header/2'
    LOADING_HUNTER_HEADER_3 = '#event:loading/hunter/header/3'
    LOADING_HUNTER_HEADER_4 = '#event:loading/hunter/header/4'
    LOADING_HUNTER_HEADER_5 = '#event:loading/hunter/header/5'
    LOADING_BOSS_HEADER_1 = '#event:loading/boss/header/1'
    LOADING_BOSS_HEADER_2 = '#event:loading/boss/header/2'
    LOADING_BOSS_HEADER_3 = '#event:loading/boss/header/3'
    LOADING_BOSS_HEADER_4 = '#event:loading/boss/header/4'
    CHARACTERISTICSPANEL_PROS = '#event:characteristicsPanel/pros'
    CHARACTERISTICSPANEL_CONS = '#event:characteristicsPanel/cons'
    CHARACTERISTICSPANEL_FEATURES = '#event:characteristicsPanel/features'
    CHARACTERISTICSPANEL_SPECIALINFO_BOSS = '#event:characteristicsPanel/specialInfo/boss'
    CHARACTERISTICSPANEL_SPECIALINFO_HUNTER_1 = '#event:characteristicsPanel/specialInfo/hunter_1'
    CHARACTERISTICSPANEL_SPECIALINFO_HUNTER_2 = '#event:characteristicsPanel/specialInfo/hunter_2'
    CHARACTERISTICSPANEL_SPECIALINFO_HUNTER_3 = '#event:characteristicsPanel/specialInfo/hunter_3'
    TTX_DURABILITY = '#event:ttx/durability'
    TTX_DESCRIPTION_DURABILITY = '#event:ttx/description/durability'
    TTX_DPM = '#event:ttx/dpm'
    TTX_DESCRIPTION_DPM = '#event:ttx/description/dpm'
    TTX_MOBILITY = '#event:ttx/mobility'
    TTX_DESCRIPTION_MOBILITY = '#event:ttx/description/mobility'
    TTX_DAMAGE = '#event:ttx/damage'
    TTX_DESCRIPTION_DAMAGE = '#event:ttx/description/damage'
    TTX_SPEED = '#event:ttx/speed'
    TTX_DESCRIPTION_SPEED = '#event:ttx/description/speed'
    TTX_ARMOR = '#event:ttx/armor'
    TTX_DESCRIPTION_ARMOR = '#event:ttx/description/armor'
    TTX_REVOLVER = '#event:ttx/revolver'
    TTX_DESCRIPTION_REVOLVER = '#event:ttx/description/revolver'
    TICKETTOOLTIP_TITLE = '#event:ticketTooltip/title'
    TICKETTOOLTIP_DESCRIPTION = '#event:ticketTooltip/description'
    TICKETTOOLTIP_QUANTITY = '#event:ticketTooltip/quantity'
    TICKETTOOLTIP_RECEIVETITLE = '#event:ticketTooltip/receiveTitle'
    TICKETTOOLTIP_RECEIVETEXT = '#event:ticketTooltip/receiveText'
    TICKETTOOLTIP_RECEIVEADDITIONALTEXT = '#event:ticketTooltip/receiveAdditionalText'
    LOOTBOXTOOLTIP_TITLE_HUNTER = '#event:lootBoxTooltip/title/hunter'
    LOOTBOXTOOLTIP_TITLE_BOSS = '#event:lootBoxTooltip/title/boss'
    LOOTBOXTOOLTIP_HOWITWORKS_TITLE = '#event:lootBoxTooltip/howItWorks/title'
    LOOTBOXTOOLTIP_HOWITWORKS_DESCRIPTION_HUNTER = '#event:lootBoxTooltip/howItWorks/description/hunter'
    LOOTBOXTOOLTIP_HOWITWORKS_DESCRIPTION_BOSS = '#event:lootBoxTooltip/howItWorks/description/boss'
    LOOTBOXTOOLTIP_HOWITWORKS_REWARD = '#event:lootBoxTooltip/howItWorks/reward'
    LOOTBOXTOOLTIP_HOWITWORKS_REWARDHIGHLIGHTED = '#event:lootBoxTooltip/howItWorks/rewardHighlighted'
    LOOTBOXTOOLTIP_HOWTOGET_TITLE = '#event:lootBoxTooltip/howToGet/title'
    LOOTBOXTOOLTIP_HOWTOGET_DESCRIPTION_HUNTER = '#event:lootBoxTooltip/howToGet/description/hunter'
    LOOTBOXTOOLTIP_HOWTOGET_DESCRIPTION_BOSS = '#event:lootBoxTooltip/howToGet/description/boss'
    PORTALAWARD_TITLE = '#event:portalAward/title'
    PORTALAWARD_TITLETANK = '#event:portalAward/titleTank'
    PORTALAWARD_ACCEPTBUTTON = '#event:portalAward/acceptButton'
    PORTALAWARD_BACKTOPORTALBUTTON = '#event:portalAward/backToPortalButton'
    PORTALAWARD_BACKTO = '#event:portalAward/backTo'
    PORTALAWARD_OPENONEMOREBUTTON = '#event:portalAward/OpenOneMoreButton'
    PORTALAWARD_OPENMOREBUTTON = '#event:portalAward/openMoreButton'
    PORTALAWARD_OPENLASTBUTTON = '#event:portalAward/OpenLastButton'
    PORTALAWARD_DESCRIPTION = '#event:portalAward/description'
    PORTALAWARD_HIGHLIGHTDESCRIPTIONHUNTER = '#event:portalAward/highlightDescriptionHunter'
    PORTALAWARD_HIGHLIGHTDESCRIPTIONBOSS = '#event:portalAward/highlightDescriptionBoss'
    PORTALAWARD_ADDITIONALTITLE = '#event:portalAward/additionalTitle'
    PORTALAWARD_MULTIPLYOPEN_ROWTEXT = '#event:portalAward/multiplyOpen/rowText'
    AWARD_VALUE = '#event:award/value'
    VEHICLEPORTAL_BACKTOPORTALBUTTON = '#event:vehiclePortal/backToPortalButton'
    VEHICLEPORTAL_OPENGARAGEBUTTON = '#event:vehiclePortal/openGarageButton'
    VEHICLEPORTAL_OPENALLREWARDSBUTTON = '#event:vehiclePortal/openAllRewardsButton'
    AWARDVIEW_BACKTOAWARDS = '#event:awardView/backToAwards'
    POSTBATTLE_BUTTON_WTEVENT_TICKET = '#event:postbattle/button/wtevent_ticket'
    POSTBATTLE_BUTTON_BOSS_COLLECTION = '#event:postbattle/button/boss_collection'
    POSTBATTLE_BUTTON_HUNTER_COLLECTION = '#event:postbattle/button/hunter_collection'
    POSTBATTLE_BUTTON_WT_HUNTER = '#event:postbattle/button/wt_hunter'
    POSTBATTLE_BUTTON_WT_BOSS = '#event:postbattle/button/wt_boss'
    POSTBATTLE_LABEL_WT_HUNTER = '#event:postbattle/label/wt_hunter'
    POSTBATTLE_LABEL_WT_BOSS = '#event:postbattle/label/wt_boss'
    POSTBATTLE_LABEL_WTEVENT_TICKET = '#event:postbattle/label/wtevent_ticket'
    POSTBATTLE_LABEL_BOSS_COLLECTION = '#event:postbattle/label/boss_collection'
    POSTBATTLE_LABEL_HUNTER_COLLECTION = '#event:postbattle/label/hunter_collection'
    POSTBATTLE_BOXAMOUNT = '#event:postbattle/boxAmount'
    POSTBATTLE_REWARD = '#event:postbattle/reward'
    POSTBATTLE_STATUS = '#event:postbattle/status'
    POSTBATTLE_REWARDRECEIVED = '#event:postbattle/rewardReceived'
    BOSS_WIDGET_SHIELD_STAGE4 = '#event:boss/widget/shield/stage4'
    BOSS_WIDGET_SHIELD_STAGE3 = '#event:boss/widget/shield/stage3'
    BOSS_WIDGET_SHIELD_STAGE2 = '#event:boss/widget/shield/stage2'
    BOSS_WIDGET_SHIELD_STAGE1 = '#event:boss/widget/shield/stage1'
    STATS_TEAM_BOSS = '#event:stats/team/boss'
    STATS_TEAM_HUNTERS = '#event:stats/team/hunters'
    PBT_VICTORY_1_1 = '#event:pbt/victory/1/1'
    PBT_VICTORY_1_3 = '#event:pbt/victory/1/3'
    PBT_VICTORY_2_1 = '#event:pbt/victory/2/1'
    PBT_DEFEAT_1_1 = '#event:pbt/defeat/1/1'
    PBT_DEFEAT_2_1 = '#event:pbt/defeat/2/1'
    PBT_DEFEAT_2_3 = '#event:pbt/defeat/2/3'
    NOTIFICATIONS_LOOTBOXES_HEADER = '#event:notifications/lootboxes/header'
    NOTIFICATIONS_LOOTBOXES_SWITCHON_BODY = '#event:notifications/lootboxes/switchOn/body'
    NOTIFICATIONS_LOOTBOXES_SWITCHON_OPENBTNLABEL = '#event:notifications/lootboxes/switchOn/openBtnLabel'
    NOTIFICATIONS_LOOTBOXES_SWITCHOFF_BODY = '#event:notifications/lootboxes/switchOff/body'
    NOTIFICATIONS_PRIMETIME_NOTAVAILABLE_HEADER = '#event:notifications/primeTime/notAvailable/header'
    NOTIFICATIONS_PRIMETIME_NOTAVAILABLE_BODY = '#event:notifications/primeTime/notAvailable/body'
    NOTIFICATIONS_PRIMETIME_AVAILABLE_HEADER = '#event:notifications/primeTime/available/header'
    NOTIFICATIONS_PRIMETIME_AVAILABLE_BODY = '#event:notifications/primeTime/available/body'
    NOTIFICATIONS_NOTSET = '#event:notifications/notSet'
    NOTIFICATIONS_TICKETTOKEN_RECEIVED_HEADER = '#event:notifications/ticketToken/received/header'
    NOTIFICATIONS_TICKETTOKEN_RECEIVED_BODY = '#event:notifications/ticketToken/received/body'
    NOTIFICATIONS_TICKETTOKEN_WITHDRAWN_BODY = '#event:notifications/ticketToken/withdrawn/body'
    NOTIFICATIONS_QUICKBOSSTICKETTOKEN_WITHDRAWN_BODY = '#event:notifications/quickBossTicketToken/withdrawn/body'
    NOTIFICATIONS_TICKETTOKEN_WITHDRAWN_OPENQUESTSBTN = '#event:notifications/ticketToken/withdrawn/openQuestsBtn'
    NOTIFICATIONS_TICKETTOKEN_WITHDRAWN_OPENPURCHASINGBTN = '#event:notifications/ticketToken/withdrawn/openPurchasingBtn'
    NOTIFICATIONS_PROGRESSION_HEADER = '#event:notifications/progression/header'
    NOTIFICATIONS_PROGRESSION_OPENBTNLABEL = '#event:notifications/progression/openBtnLabel'
    NOTIFICATIONS_PROGRESSION_STAGEACHIEVED = '#event:notifications/progression/stageAchieved'
    NOTIFICATIONS_PROGRESSION_COMPLETED = '#event:notifications/progression/completed'
    NOTIFICATIONS_SWITCHON_HEADER = '#event:notifications/switchOn/header'
    NOTIFICATIONS_SWITCHON_BODY = '#event:notifications/switchOn/body'
    NOTIFICATIONS_SWITCHOFF_HEADER = '#event:notifications/switchOff/header'
    NOTIFICATIONS_SWITCHOFF_BODY = '#event:notifications/switchOff/body'
    NOTIFICATIONS_EVENTSTART_BODY = '#event:notifications/eventStart/body'
    NOTIFICATIONS_EVENTSTART_OPENBTNLABEL = '#event:notifications/eventStart/openBtnLabel'
    NOTIFICATIONS_EVENTEND_BODY = '#event:notifications/eventEnd/body'
    NOTIFICATIONS_BATTLERESULTS_VICTORY_HEADER = '#event:notifications/battleResults/victory/header'
    NOTIFICATIONS_BATTLERESULTS_DEFEAT_HEADER = '#event:notifications/battleResults/defeat/header'
    NOTIFICATIONS_BATTLERESULTS_BUTTONLABEL = '#event:notifications/battleResults/buttonLabel'
    NOTIFICATIONS_BATTLERESULTS_EVENT = '#event:notifications/battleResults/event'
    NOTIFICATIONS_BATTLERESULTS_EVENTNAME = '#event:notifications/battleResults/eventName'
    NOTIFICATIONS_BATTLERESULTS_BATTLE = '#event:notifications/battleResults/battle'
    NOTIFICATIONS_BATTLERESULTS_TEAM = '#event:notifications/battleResults/team'
    NOTIFICATIONS_BATTLERESULTS_TEAM_BOSS = '#event:notifications/battleResults/team/boss'
    NOTIFICATIONS_BATTLERESULTS_TEAM_HUNTERS = '#event:notifications/battleResults/team/hunters'
    NOTIFICATIONS_BATTLERESULTS_QUESTCOMPLETED = '#event:notifications/battleResults/questCompleted'
    NOTIFICATIONS_BATTLERESULTS_LOOTBOXES_WT_BOSS = '#event:notifications/battleResults/lootboxes/wt_boss'
    NOTIFICATIONS_BATTLERESULTS_LOOTBOXES_WT_HUNTER = '#event:notifications/battleResults/lootboxes/wt_hunter'
    NOTIFICATIONS_LOOTBOXAUTOOPEN_WT_HUNTER = '#event:notifications/lootboxAutoOpen/wt_hunter'
    NOTIFICATIONS_LOOTBOXAUTOOPEN_WT_BOSS = '#event:notifications/lootboxAutoOpen/wt_boss'
    NOTIFICATIONS_BATTLERESULTS_DISABLEINQUEUE = '#event:notifications/battleResults/disableInQueue'
    NOTIFICATIONS_BATTLERESULTS_DISABLENOTINPREBATTLE = '#event:notifications/battleResults/disableNotInPrebattle'
    STUN_INDICATOR = '#event:stun/indicator'
    BOMBCAPTURE_INDICATOR = '#event:bombCapture/indicator'
    BOMBDEPLOY_INDICATOR = '#event:bombDeploy/indicator'
    BOMBABSORB_INDICATOR = '#event:bombAbsorb/indicator'
    BOMBCARRY_HINT = '#event:bombCarry/hint'
    BATTLEHINTS_WTBATTLESTART_HUNTERS = '#event:battleHints/wtBattleStart_hunters'
    BATTLEHINTS_WTBATTLESTART_BOSS = '#event:battleHints/wtBattleStart_boss'
    BATTLEHINTS_WTCAMPKILLED_HUNTERS = '#event:battleHints/wtCampKilled_hunters'
    BATTLEHINTS_WTCAMPKILLED_BOSS = '#event:battleHints/wtCampKilled_boss'
    BATTLEHINTS_WTBOMBPICKED_HUNTERS = '#event:battleHints/wtBombPicked_hunters'
    BATTLEHINTS_WTBOMBPICKED_BOSS = '#event:battleHints/wtBombPicked_boss'
    BATTLEHINTS_WTBOMBDROPPED_HUNTERS = '#event:battleHints/wtBombDropped_hunters'
    BATTLEHINTS_WTBOMBDROPPED_BOSS = '#event:battleHints/wtBombDropped_boss'
    BATTLEHINTS_WTBOMBCONSUMED_HUNTERS = '#event:battleHints/wtBombConsumed_hunters'
    BATTLEHINTS_WTBOMBCONSUMED_BOSS = '#event:battleHints/wtBombConsumed_boss'
    BATTLEHINTS_WTBOMBEXPLODED_HUNTERS = '#event:battleHints/wtBombExploded_hunters'
    BATTLEHINTS_WTBOMBEXPLODEDHARM_BOSS = '#event:battleHints/wtBombExplodedHarm_boss'
    BATTLEHINTS_WTBOMBEXPLODEDNOHARM_BOSS = '#event:battleHints/wtBombExplodedNoHarm_boss'
    BATTLEHINTS_WTBOMBWASTED_HUNTERS = '#event:battleHints/wtBombWasted_hunters'
    BATTLEHINTS_WTBOMBWASTED_BOSS = '#event:battleHints/wtBombWasted_boss'
    BATTLEHINTS_WTBOSSINVINCIBLE = '#event:battleHints/wtBossInvincible'
    BATTLEHINTS_WTHUNTERRESPAWNED = '#event:battleHints/wtHunterRespawned'
    BATTLEHINTS_WTHUNTERRESPAWNEDLAST = '#event:battleHints/wtHunterRespawnedLast'
    BATTLEHINTS_WTHUNTERISDEAD = '#event:battleHints/wtHunterIsDead'
    BATTLEHINTS_WTENDGAMESTART_HUNTERS = '#event:battleHints/wtEndgameStart_hunters'
    BATTLEHINTS_WTENDGAMESTARTHARM_BOSS = '#event:battleHints/wtEndgameStartHarm_boss'
    BATTLEHINTS_WTENDGAMESTARTNOHARM_BOSS = '#event:battleHints/wtEndgameStartNoHarm_boss'
    BATTLEHINTS_WTTIMEREMAINING_HUNTER = '#event:battleHints/wtTimeRemaining_hunter'
    BATTLEHINTS_WTTIMEREMAINING_BOSS = '#event:battleHints/wtTimeRemaining_boss'
    BATTLEHINTS_WTOVERTIME = '#event:battleHints/wtOvertime'
    BATTLEHINTS_WTBOSSTELEPORT = '#event:battleHints/wtBossTeleport'
    BATTLEHINTS_WTGENERATORSPAWNED_HUNTERS = '#event:battleHints/wtGeneratorSpawned_hunters'
    BATTLEHINTS_WTGENERATORSPAWNED_BOSS = '#event:battleHints/wtGeneratorSpawned_boss'
    BATTLEHINTS_WTGENERATORSPAWNED_TIME = '#event:battleHints/wtGeneratorSpawned_time'
    BATTLEHINTS_WTGENERATORACTIVATED_HUNTERS = '#event:battleHints/wtGeneratorActivated_hunters'
    BATTLEHINTS_WTGENERATORACTIVATED_BOSS = '#event:battleHints/wtGeneratorActivated_boss'
    BATTLEHINTS_WTCAMPSSPAWNED_HUNTERS = '#event:battleHints/wtCampsSpawned_hunters'
    BATTLEHINTS_WTCAMPSSPAWNED_BOSS = '#event:battleHints/wtCampsSpawned_boss'
    PLAYERSPANEL_CAMPLABEL = '#event:playersPanel/campLabel'
    PLAYERSPANEL_BOMBLABEL = '#event:playersPanel/bombLabel'
    PLAYERSPANEL_BOTNAME = '#event:playersPanel/botName'
    POSTBATTLE_SCREEN_BOTNAME = '#event:postbattle_screen/botName'
    LOADING_BATTLETYPES_WT = '#event:loading/battleTypes/wt'
    LOADING_WINTEXT_BOSS = '#event:loading/winText/boss'
    LOADING_WINTEXT_HUNTERS = '#event:loading/winText/hunters'
    HUNTERRESPAWN_TIMERTEXT = '#event:hunterRespawn/timerText'
    HUNTERRESPAWN_HINTTEXT = '#event:hunterRespawn/hintText'
    MINIMAP_RESPAWNENTRY_HINTTEXT = '#event:minimap/respawnEntry/hintText'
    BATTLETIMER_OVERTIME_MESSAGETEXT = '#event:battleTimer/overtime/messageText'
    BATTLETIMER_TIMEREMAINING_HUNTER_MESSAGETEXT = '#event:battleTimer/timeRemaining/hunter/messageText'
    BATTLETIMER_TIMEREMAINING_BOSS_MESSAGETEXT = '#event:battleTimer/timeRemaining/boss/messageText'
    TEAMBASEPANEL_CAPTURING = '#event:teamBasePanel/capturing'
    HANGAR_STARTBTN_EVENTSQUADNOTREADY_WRONGVEHICLECOUNT_HEADER = '#event:hangar/startBtn/eventSquadNotReady/wrongVehicleCount/header'
    HANGAR_STARTBTN_EVENTSQUADNOTREADY_WRONGVEHICLECOUNT_BODY = '#event:hangar/startBtn/eventSquadNotReady/wrongVehicleCount/body'
    ALL_ENUM = (PUNISHMENTWINDOW_REASON_EVENT_DESERTER,
     PUNISHMENTWINDOW_REASON_EVENT_AFK,
     BATTLEHINTS_TESTMESSAGE,
     BATTLEHINTS_TESTMESSAGEWITHPARAMS,
     CRAFTMACHINE_TITLE,
     CRAFTMACHINE_SUBTITLE,
     CRAFTMACHINE_STATUSDATE,
     MENU_SELECTOR_TITLE,
     MENU_SELECTOR_UNAVAILABLE,
     TOOLTIPS_SELECTOR_TITLE,
     TOOLTIPS_SELECTOR_DESC,
     TOOLTIPS_SELECTOR_TIMETABLE_TITLE,
     TOOLTIPS_SELECTOR_TIMETABLE_TODAY,
     TOOLTIPS_SELECTOR_TIMETABLE_TOMORROW,
     TOOLTIPS_SELECTOR_TIMETABLE_EMPTY,
     TOOLTIPS_SELECTOR_TIMETABLE_TILLEND,
     SELECTORTOOLTIP_TIMETABLE_TITLE,
     SELECTORTOOLTIP_TIMETABLE_TILLEND,
     QUESTS_ERROR_NO_TICKET,
     QUESTS_ERROR_NO_TICKET_TOOLTIP_HEADER,
     QUESTS_ERROR_NO_TICKET_TOOLTIP_BODY,
     TOOLTIPS_HEADER_QUESTS_HEADER_EVENT_HUNTER,
     TOOLTIPS_HEADER_QUESTS_HEADER_EVENT_BOSS,
     TOOLTIPS_HEADER_QUESTS_HEADER_DESCRIPTION_TILL_END,
     TOOLTIPS_HEADER_QUESTS_HEADER_DESCRIPTION_TILL_UPD,
     TOOLTIPS_HEADER_QUESTS_HEADER_UNAVAILABLE,
     TOOLTIPS_HEADER_QUESTS_HEADER_DESCRIPTION_UNAVAILABLE,
     TOOLTIPS_HEADER_QUESTS_HEADER_SPECIAL_EVENT_BOSS,
     TOOLTIPS_HEADER_QUESTS_BOTTOM,
     CALENDARDAY_TITLE,
     CALENDARDAY_SERVERNAME,
     CALENDARDAY_TIME,
     STATUS_TIMELEFT_DAYS,
     STATUS_TIMELEFT_HOURS,
     STATUS_TIMELEFT_LESSHOUR,
     STATUS_TIMELEFT_MIN,
     STATUS_TIMELEFT_LESSMIN,
     STATUS_UNAVAILABLE,
     WTEVENTSENTRYPOINT_TITLE,
     WTEVENTSENTRYPOINT_ACTIVE,
     WTEVENTSENTRYPOINT_FROZEN,
     WTEVENTAWARDSVIEW_MAINREWARDS_BUTTON,
     WTEVENTAWARDSVIEW_MAINREWARDS_BACK_PORTAL,
     WTEVENTAWARDSVIEW_MAINREWARDS_PREMIUM_PLUS,
     WTEVENTAWARDSVIEW_MAINREWARDS_WT_BOSS,
     WTEVENTAWARDSVIEW_DESCIPTION,
     WTEVENTAWARDSVIEW_TITLE,
     WTEVENTAWARDSVIEW_STATUS_PART,
     WTEVENTAWARDSVIEW_STATUS_ALL,
     WTEVENTAWARDSVIEW_STATUS_POSTBATTLE,
     WINDOW_UNIT_MESSAGE_VEHICLENOTSELECTED,
     SIMPLESQUAD_SELECTRESTRICTION,
     WTEVENTWELCOMEVIEW_WELCOME_TITLE,
     WTEVENTWELCOMEVIEW_WELCOME_COLLECTION_TITLE,
     WTEVENTWELCOMEVIEW_WELCOME_COLLECTION_TEXT,
     WTEVENTWELCOMEVIEW_WELCOME_ASYMMETRY_TITLE,
     WTEVENTWELCOMEVIEW_WELCOME_ASYMMETRY_TEXT,
     WTEVENTWELCOMEVIEW_WELCOME_WT_WELCOME_TITLE,
     WTEVENTWELCOMEVIEW_WELCOME_WT_WELCOME_TEXT,
     WTEVENTWELCOMEVIEW_WELCOME_CONFIRM_BTN,
     WTEVENTAMMUNITIONTOOLTIPVIEW_ADDITIONALINFOTITLE,
     WTEVENTLOOTBOXESINFOVIEW_TOOLTIP_TITLE,
     WTEVENTLOOTBOXESINFOVIEW_TOOLTIP_HUNTERSUBTITLE,
     WTEVENTLOOTBOXESINFOVIEW_TOOLTIP_HUNTERTEXT,
     WTEVENTLOOTBOXESINFOVIEW_TOOLTIP_BOSSSUBTITLE,
     WTEVENTLOOTBOXESINFOVIEW_TOOLTIP_BOSSTEXT,
     WTEVENTSCAROUSELVIEW_INBATTLETEXT,
     WTEVENTSCAROUSELVIEW_INPLATOONTEXT,
     WTEVENTSCAROUSELVIEW_UNSUITABLETEXT,
     WTEVENTSCAROUSELVIEW_TICKETNEEDEDTEXT,
     WTEVENTSTICKETMESSAGEVIEW_BOSS_DESCRIPTION,
     WTEVENTSTICKETMESSAGEVIEW_BUYTEXT,
     WTEVENTSTICKETMESSAGEVIEW_TASKTEXT,
     WTEVENTPORTALS_MAINTITLE,
     WTEVENTPORTALS_WARNING,
     WTEVENTPORTALS_PRICE,
     WTEVENTPORTALS_BUYBUTTON,
     WTEVENTPORTALS_BUYBUTTONCNTEXT,
     WTEVENTPORTALS_BUYBUTTONTOOLTIP,
     WTEVENTPORTALS_TITLE_HUNTER,
     WTEVENTPORTALS_TEXT_HUNTER,
     WTEVENTPORTALS_SUBTITLE_HUNTER,
     WTEVENTPORTALS_DESCRIPTION_HUNTER,
     WTEVENTPORTALS_TITLE_BOSS,
     WTEVENTPORTALS_TEXT_BOSS,
     WTEVENTPORTALS_BOSS_LEFT,
     WTEVENTPORTALS_BOSS_ONELEFT,
     WTEVENTPORTALS_TITLE_TANK,
     WTEVENTPORTALS_TEXT_TANK,
     WTEVENTPORTALS_TANKINHANGAR,
     WTEVENTPORTALS_SUBTITLE_BOSS,
     WTEVENTPORTALS_DESCRIPTION_BOSS,
     WTEVENTPORTALS_INSIDE_BACKBUTTON,
     WTEVENTPORTALS_INSIDE_SUBTITLE,
     WTEVENTPORTALS_INSIDE_NUMBERING,
     WTEVENTPORTALS_INSIDE_HIGHPROBABILITY,
     WTEVENTPORTALS_INSIDE_GUARANTEEDPROBABILITY,
     WTEVENTPORTALS_INSIDE_MEDIUMPROBABILITY,
     WTEVENTPORTALS_INSIDE_LOWPROBABILITY,
     WTEVENTPORTALS_INSIDE_LOWPROBABILITYTANK,
     WTEVENTPORTALS_INSIDE_SHOWANIMATION,
     WTEVENTPORTALS_INSIDE_TIMES,
     WTEVENTPORTALS_INSIDE_PLURALTIMES,
     WTEVENTPORTALS_INSIDE_BUTTONRUNPORTAL,
     WTEVENTPORTALS_INSIDE_BUTTONTAKETANK,
     WTEVENTPORTALS_INSIDE_CURRENTKEYSAMOUNT_HUNTER,
     WTEVENTPORTALS_INSIDE_CURRENTKEYSAMOUNT_BOSS,
     WTEVENTPORTALS_INSIDE_CURRENTKEYSAMOUNTIS0_HUNTER,
     WTEVENTPORTALS_INSIDE_CURRENTKEYSAMOUNTIS0_BOSS,
     WTEVENTPORTALS_INSIDE_REWARDS_HUNTERCOLLECTIONELEMENT,
     WTEVENTPORTALS_INSIDE_REWARDS_BOSSKEY,
     WTEVENTPORTALS_INSIDE_REWARDS_STYLE3D,
     WTEVENTPORTALS_INSIDE_REWARDS_TANK,
     WTEVENTPORTALS_INSIDE_REWARDS_TANKS,
     WTEVENTPORTALS_INSIDE_REWARDS_TANKSSEPARATOR,
     WTEVENTPORTALS_INSIDE_REWARDS_TANKSTOOLTIP_HEADER,
     WTEVENTPORTALS_INSIDE_REWARDS_TANKSTOOLTIP_BODY,
     WTEVENTPORTALS_INSIDE_REWARDS_TANKDESCRIPTION,
     WTGUARANTEEDREWARDTOOLTIPVIEW_TITLE,
     WTGUARANTEEDREWARDTOOLTIPVIEW_PORTALRUNS,
     WTGUARANTEEDREWARDTOOLTIPVIEW_DESCRIPTION,
     WTGUARANTEEDREWARDTOOLTIPVIEW_PORTALRUNSLEFT,
     WTGUARANTEEDREWARDTOOLTIPVIEW_VEHICLESTITLE,
     WTGUARANTEEDREWARDTOOLTIPVIEW_VEHICLESDESCRIPTION,
     WTEVENTPORTALS_COLLECTIONTOOLTIP_HUNTERCOLLECTION_TITLE,
     WTEVENTPORTALS_COLLECTIONTOOLTIP_HUNTERCOLLECTION_DESCRIPTION,
     WTEVENTPORTALS_COLLECTIONTOOLTIP_HUNTERCOLLECTION_STATUS_NOTCOLLECTED,
     WTEVENTPORTALS_COLLECTIONTOOLTIP_HUNTERCOLLECTION_STATUS_COLLECTED,
     WTEVENTPORTALS_COLLECTIONTOOLTIP_RANDOMSTYLE2D_TITLE,
     WTEVENTPORTALS_COLLECTIONTOOLTIP_RANDOMSTYLE2D_DESCRIPTION,
     WTEVENTPORTALS_COLLECTIONTOOLTIP_RANDOMDECAL_TITLE,
     WTEVENTPORTALS_COLLECTIONTOOLTIP_RANDOMDECAL_DESCRIPTION,
     WTEVENTPORTALS_COLLECTIONTOOLTIP_RANDOMSTYLE3D_TITLE,
     WTEVENTPORTALS_COLLECTIONTOOLTIP_RANDOMSTYLE3D_DESCRIPTION,
     WTEVENTPORTALS_COLLECTIONTOOLTIP_RANDOMSTYLE3D_STATUS_NOTCOLLECTED,
     WTEVENTPORTALS_COLLECTIONTOOLTIP_RANDOMSTYLE3D_STATUS_COLLECTED,
     WTEVENTBUYLOOTBOXESTOOLTIPVIEW_TITLE,
     WTEVENTBUYLOOTBOXESTOOLTIPVIEW_DESCRIPTION,
     WTEVENTBUYLOOTBOXESTOOLTIPVIEW_AMOUNTLEFT,
     WTEVENTBUYLOOTBOXESTOOLTIPVIEW_INFO,
     WTEVENTBUYLOOTBOXESTOOLTIPVIEW_ADDITIONALINFO,
     BONUSTOOLTIP_GOLD_HEADER,
     BONUSTOOLTIP_GOLD_BODY,
     BONUSTOOLTIP_CREWBOOKS_HEADER,
     BONUSTOOLTIP_CREWBOOKS_BODY,
     BONUSTOOLTIP_BOOSTER_CREDITS_HEADER,
     BONUSTOOLTIP_BOOSTER_CREDITS_BODY,
     BONUSTOOLTIP_BOOSTER_CREW_XP_HEADER,
     BONUSTOOLTIP_BOOSTER_CREW_XP_BODY,
     BONUSTOOLTIP_BOOSTER_FREE_XP_HEADER,
     BONUSTOOLTIP_BOOSTER_FREE_XP_BODY,
     BONUSTOOLTIP_BOOSTER_XP_HEADER,
     BONUSTOOLTIP_BOOSTER_XP_BODY,
     ELEMENTBONUS_DESC_STYLE3D,
     BONUSNAME_SLOTS,
     COLLECTION_TITLE,
     COLLECTION_ABOUT,
     COLLECTION_COLLECTED,
     COLLECTION_COLLECTEDALL,
     TOOLTIPS_TITLE,
     TOOLTIPS_SUBTITLE,
     TOOLTIPS_PROGRESS_TEXT,
     TOOLTIPS_COMPLETE_TEXT,
     TOOLTIPS_FOOTER_FIRST_COLECTION,
     TOOLTIPS_FOOTER_SECOND_COLECTION,
     COLLECTIONTOOLTIP_TITLE_HUNTER,
     COLLECTIONTOOLTIP_TITLEFINAL_HUNTER,
     COLLECTIONTOOLTIP_DESCRIPTION_HUNTER,
     COLLECTIONTOOLTIP_FINALDESCRIPTION_HUNTER,
     COLLECTIONTOOLTIP_TITLE_BOSS,
     COLLECTIONTOOLTIP_TITLEFINAL_BOSS,
     COLLECTIONTOOLTIP_DESCRIPTION_BOSS,
     COLLECTIONTOOLTIP_FINALDESCRIPTION_BOSS,
     BATTLEQUEUE_WIDGET_BTNLABEL,
     BATTLEQUEUE_WIDGET_CALCULATEDTEXT,
     BATTLEQUEUE_WIDGET_CHANGETITLE,
     BATTLEQUEUE_WIDGET_OFFERHUNTERTTILE,
     BATTLEQUEUE_WIDGET_TICKETTEXT,
     BATTLEQUEUE_WIDGET_BONUS,
     BATTLEQUEUE_AVGWAITTIME_LABEL,
     BATTLEQUEUE_WIDGET_BONUSDESCR,
     VEHICLE_TAGS_EVENT_BOSS_NAME,
     VEHICLE_TAGS_EVENT_HUNTER_NAME,
     PRIMETIME_TITLE,
     PRIMETIME_STATUS_ALLSERVERSDISABLED,
     PRIMETIME_STATUS_UNTILL,
     PRIMETIME_STATUS_DISABLEFIRST,
     PRIMETIME_ENDOFCYCLE,
     PRIMETIME_STATUS_PRIMEISAVAILABLE,
     PRIMETIME_STATUS_PRIMEWILLBEAVAILABLE,
     PRIMETIME_SERVERTOOLTIP,
     PRIMETIME_SERVERUNAVAILABLETOOLTIP,
     SERVERALERTMESSAGE,
     SERVERALERTMESSAGE_BUTTON,
     CREWPANEL_ROLE_BOSS,
     CREWPANEL_SLOGAN_BOSS,
     CREWPANEL_ROLE_HUNTER_1,
     CREWPANEL_SLOGAN_HUNTER_1,
     CREWPANEL_ROLE_HUNTER_2,
     CREWPANEL_SLOGAN_HUNTER_2,
     CREWPANEL_ROLE_HUNTER_3,
     CREWPANEL_SLOGAN_HUNTER_3,
     TANKMANTOOLTIP_STATUS_BOSS,
     TANKMANTOOLTIP_STATUS_HUNTER,
     TANKMANTOOLTIP_BOSS_DESCR,
     TANKMANTOOLTIP_HUNTER_1_DESCR,
     TANKMANTOOLTIP_HUNTER_2_DESCR,
     TANKMANTOOLTIP_HUNTER_3_DESCR,
     TANKMANTOOLTIP_SKILLSTITLE,
     BONUSES_HUNTER_COLLECTION_TOOLTIP_HEADER,
     BONUSES_HUNTER_COLLECTION_TOOLTIP_BODY,
     BONUSES_BOSS_COLLECTION_TOOLTIP_HEADER,
     BONUSES_BOSS_COLLECTION_TOOLTIP_BODY,
     LOADING_HUNTER_HEADER_1,
     LOADING_HUNTER_HEADER_2,
     LOADING_HUNTER_HEADER_3,
     LOADING_HUNTER_HEADER_4,
     LOADING_HUNTER_HEADER_5,
     LOADING_BOSS_HEADER_1,
     LOADING_BOSS_HEADER_2,
     LOADING_BOSS_HEADER_3,
     LOADING_BOSS_HEADER_4,
     CHARACTERISTICSPANEL_PROS,
     CHARACTERISTICSPANEL_CONS,
     CHARACTERISTICSPANEL_FEATURES,
     CHARACTERISTICSPANEL_SPECIALINFO_BOSS,
     CHARACTERISTICSPANEL_SPECIALINFO_HUNTER_1,
     CHARACTERISTICSPANEL_SPECIALINFO_HUNTER_2,
     CHARACTERISTICSPANEL_SPECIALINFO_HUNTER_3,
     TTX_DURABILITY,
     TTX_DESCRIPTION_DURABILITY,
     TTX_DPM,
     TTX_DESCRIPTION_DPM,
     TTX_MOBILITY,
     TTX_DESCRIPTION_MOBILITY,
     TTX_DAMAGE,
     TTX_DESCRIPTION_DAMAGE,
     TTX_SPEED,
     TTX_DESCRIPTION_SPEED,
     TTX_ARMOR,
     TTX_DESCRIPTION_ARMOR,
     TTX_REVOLVER,
     TTX_DESCRIPTION_REVOLVER,
     TICKETTOOLTIP_TITLE,
     TICKETTOOLTIP_DESCRIPTION,
     TICKETTOOLTIP_QUANTITY,
     TICKETTOOLTIP_RECEIVETITLE,
     TICKETTOOLTIP_RECEIVETEXT,
     TICKETTOOLTIP_RECEIVEADDITIONALTEXT,
     LOOTBOXTOOLTIP_TITLE_HUNTER,
     LOOTBOXTOOLTIP_TITLE_BOSS,
     LOOTBOXTOOLTIP_HOWITWORKS_TITLE,
     LOOTBOXTOOLTIP_HOWITWORKS_DESCRIPTION_HUNTER,
     LOOTBOXTOOLTIP_HOWITWORKS_DESCRIPTION_BOSS,
     LOOTBOXTOOLTIP_HOWITWORKS_REWARD,
     LOOTBOXTOOLTIP_HOWITWORKS_REWARDHIGHLIGHTED,
     LOOTBOXTOOLTIP_HOWTOGET_TITLE,
     LOOTBOXTOOLTIP_HOWTOGET_DESCRIPTION_HUNTER,
     LOOTBOXTOOLTIP_HOWTOGET_DESCRIPTION_BOSS,
     PORTALAWARD_TITLE,
     PORTALAWARD_TITLETANK,
     PORTALAWARD_ACCEPTBUTTON,
     PORTALAWARD_BACKTOPORTALBUTTON,
     PORTALAWARD_BACKTO,
     PORTALAWARD_OPENONEMOREBUTTON,
     PORTALAWARD_OPENMOREBUTTON,
     PORTALAWARD_OPENLASTBUTTON,
     PORTALAWARD_DESCRIPTION,
     PORTALAWARD_HIGHLIGHTDESCRIPTIONHUNTER,
     PORTALAWARD_HIGHLIGHTDESCRIPTIONBOSS,
     PORTALAWARD_ADDITIONALTITLE,
     PORTALAWARD_MULTIPLYOPEN_ROWTEXT,
     AWARD_VALUE,
     VEHICLEPORTAL_BACKTOPORTALBUTTON,
     VEHICLEPORTAL_OPENGARAGEBUTTON,
     VEHICLEPORTAL_OPENALLREWARDSBUTTON,
     AWARDVIEW_BACKTOAWARDS,
     POSTBATTLE_BUTTON_WTEVENT_TICKET,
     POSTBATTLE_BUTTON_BOSS_COLLECTION,
     POSTBATTLE_BUTTON_HUNTER_COLLECTION,
     POSTBATTLE_BUTTON_WT_HUNTER,
     POSTBATTLE_BUTTON_WT_BOSS,
     POSTBATTLE_LABEL_WT_HUNTER,
     POSTBATTLE_LABEL_WT_BOSS,
     POSTBATTLE_LABEL_WTEVENT_TICKET,
     POSTBATTLE_LABEL_BOSS_COLLECTION,
     POSTBATTLE_LABEL_HUNTER_COLLECTION,
     POSTBATTLE_BOXAMOUNT,
     POSTBATTLE_REWARD,
     POSTBATTLE_STATUS,
     POSTBATTLE_REWARDRECEIVED,
     BOSS_WIDGET_SHIELD_STAGE4,
     BOSS_WIDGET_SHIELD_STAGE3,
     BOSS_WIDGET_SHIELD_STAGE2,
     BOSS_WIDGET_SHIELD_STAGE1,
     STATS_TEAM_BOSS,
     STATS_TEAM_HUNTERS,
     PBT_VICTORY_1_1,
     PBT_VICTORY_1_3,
     PBT_VICTORY_2_1,
     PBT_DEFEAT_1_1,
     PBT_DEFEAT_2_1,
     PBT_DEFEAT_2_3,
     NOTIFICATIONS_LOOTBOXES_HEADER,
     NOTIFICATIONS_LOOTBOXES_SWITCHON_BODY,
     NOTIFICATIONS_LOOTBOXES_SWITCHON_OPENBTNLABEL,
     NOTIFICATIONS_LOOTBOXES_SWITCHOFF_BODY,
     NOTIFICATIONS_PRIMETIME_NOTAVAILABLE_HEADER,
     NOTIFICATIONS_PRIMETIME_NOTAVAILABLE_BODY,
     NOTIFICATIONS_PRIMETIME_AVAILABLE_HEADER,
     NOTIFICATIONS_PRIMETIME_AVAILABLE_BODY,
     NOTIFICATIONS_NOTSET,
     NOTIFICATIONS_TICKETTOKEN_RECEIVED_HEADER,
     NOTIFICATIONS_TICKETTOKEN_RECEIVED_BODY,
     NOTIFICATIONS_TICKETTOKEN_WITHDRAWN_BODY,
     NOTIFICATIONS_QUICKBOSSTICKETTOKEN_WITHDRAWN_BODY,
     NOTIFICATIONS_TICKETTOKEN_WITHDRAWN_OPENQUESTSBTN,
     NOTIFICATIONS_TICKETTOKEN_WITHDRAWN_OPENPURCHASINGBTN,
     NOTIFICATIONS_PROGRESSION_HEADER,
     NOTIFICATIONS_PROGRESSION_OPENBTNLABEL,
     NOTIFICATIONS_PROGRESSION_STAGEACHIEVED,
     NOTIFICATIONS_PROGRESSION_COMPLETED,
     NOTIFICATIONS_SWITCHON_HEADER,
     NOTIFICATIONS_SWITCHON_BODY,
     NOTIFICATIONS_SWITCHOFF_HEADER,
     NOTIFICATIONS_SWITCHOFF_BODY,
     NOTIFICATIONS_EVENTSTART_BODY,
     NOTIFICATIONS_EVENTSTART_OPENBTNLABEL,
     NOTIFICATIONS_EVENTEND_BODY,
     NOTIFICATIONS_BATTLERESULTS_VICTORY_HEADER,
     NOTIFICATIONS_BATTLERESULTS_DEFEAT_HEADER,
     NOTIFICATIONS_BATTLERESULTS_BUTTONLABEL,
     NOTIFICATIONS_BATTLERESULTS_EVENT,
     NOTIFICATIONS_BATTLERESULTS_EVENTNAME,
     NOTIFICATIONS_BATTLERESULTS_BATTLE,
     NOTIFICATIONS_BATTLERESULTS_TEAM,
     NOTIFICATIONS_BATTLERESULTS_TEAM_BOSS,
     NOTIFICATIONS_BATTLERESULTS_TEAM_HUNTERS,
     NOTIFICATIONS_BATTLERESULTS_QUESTCOMPLETED,
     NOTIFICATIONS_BATTLERESULTS_LOOTBOXES_WT_BOSS,
     NOTIFICATIONS_BATTLERESULTS_LOOTBOXES_WT_HUNTER,
     NOTIFICATIONS_LOOTBOXAUTOOPEN_WT_HUNTER,
     NOTIFICATIONS_LOOTBOXAUTOOPEN_WT_BOSS,
     NOTIFICATIONS_BATTLERESULTS_DISABLEINQUEUE,
     NOTIFICATIONS_BATTLERESULTS_DISABLENOTINPREBATTLE,
     STUN_INDICATOR,
     BOMBCAPTURE_INDICATOR,
     BOMBDEPLOY_INDICATOR,
     BOMBABSORB_INDICATOR,
     BOMBCARRY_HINT,
     BATTLEHINTS_WTBATTLESTART_HUNTERS,
     BATTLEHINTS_WTBATTLESTART_BOSS,
     BATTLEHINTS_WTCAMPKILLED_HUNTERS,
     BATTLEHINTS_WTCAMPKILLED_BOSS,
     BATTLEHINTS_WTBOMBPICKED_HUNTERS,
     BATTLEHINTS_WTBOMBPICKED_BOSS,
     BATTLEHINTS_WTBOMBDROPPED_HUNTERS,
     BATTLEHINTS_WTBOMBDROPPED_BOSS,
     BATTLEHINTS_WTBOMBCONSUMED_HUNTERS,
     BATTLEHINTS_WTBOMBCONSUMED_BOSS,
     BATTLEHINTS_WTBOMBEXPLODED_HUNTERS,
     BATTLEHINTS_WTBOMBEXPLODEDHARM_BOSS,
     BATTLEHINTS_WTBOMBEXPLODEDNOHARM_BOSS,
     BATTLEHINTS_WTBOMBWASTED_HUNTERS,
     BATTLEHINTS_WTBOMBWASTED_BOSS,
     BATTLEHINTS_WTBOSSINVINCIBLE,
     BATTLEHINTS_WTHUNTERRESPAWNED,
     BATTLEHINTS_WTHUNTERRESPAWNEDLAST,
     BATTLEHINTS_WTHUNTERISDEAD,
     BATTLEHINTS_WTENDGAMESTART_HUNTERS,
     BATTLEHINTS_WTENDGAMESTARTHARM_BOSS,
     BATTLEHINTS_WTENDGAMESTARTNOHARM_BOSS,
     BATTLEHINTS_WTTIMEREMAINING_HUNTER,
     BATTLEHINTS_WTTIMEREMAINING_BOSS,
     BATTLEHINTS_WTOVERTIME,
     BATTLEHINTS_WTBOSSTELEPORT,
     BATTLEHINTS_WTGENERATORSPAWNED_HUNTERS,
     BATTLEHINTS_WTGENERATORSPAWNED_BOSS,
     BATTLEHINTS_WTGENERATORSPAWNED_TIME,
     BATTLEHINTS_WTGENERATORACTIVATED_HUNTERS,
     BATTLEHINTS_WTGENERATORACTIVATED_BOSS,
     BATTLEHINTS_WTCAMPSSPAWNED_HUNTERS,
     BATTLEHINTS_WTCAMPSSPAWNED_BOSS,
     PLAYERSPANEL_CAMPLABEL,
     PLAYERSPANEL_BOMBLABEL,
     PLAYERSPANEL_BOTNAME,
     POSTBATTLE_SCREEN_BOTNAME,
     LOADING_BATTLETYPES_WT,
     LOADING_WINTEXT_BOSS,
     LOADING_WINTEXT_HUNTERS,
     HUNTERRESPAWN_TIMERTEXT,
     HUNTERRESPAWN_HINTTEXT,
     MINIMAP_RESPAWNENTRY_HINTTEXT,
     BATTLETIMER_OVERTIME_MESSAGETEXT,
     BATTLETIMER_TIMEREMAINING_HUNTER_MESSAGETEXT,
     BATTLETIMER_TIMEREMAINING_BOSS_MESSAGETEXT,
     TEAMBASEPANEL_CAPTURING,
     HANGAR_STARTBTN_EVENTSQUADNOTREADY_WRONGVEHICLECOUNT_HEADER,
     HANGAR_STARTBTN_EVENTSQUADNOTREADY_WRONGVEHICLECOUNT_BODY)

    @classmethod
    def all(cls, key0):
        outcome = '#event:{}'.format(key0)
        if outcome not in cls.ALL_ENUM:
            LOG_WARNING('Localization key "{}" not found'.format(outcome))
            return None
        else:
            return outcome