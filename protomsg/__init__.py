from account_pb2 import *
from hero_pb2 import *
from cmd_pb2 import *
from world_pb2 import *
from guide_pb2 import *
from mail_pb2 import *
from purchase_pb2 import *
from daily_pb2 import *
from chat_pb2 import *
from task_pb2 import *
from achievement_pb2 import *
from store_pb2 import *
from character_pb2 import *
from item_pb2 import *
from levy_pb2 import *
from formation_pb2 import *
from friend_pb2 import *
from battle_pb2 import *
from prize_pb2 import *

RESPONSE_NOTIFY_TYPE = {
    "CommandResponse": 50,
    "VersionCheckResponse": 52,
    "SyncResponse": 61,
    "ResumeResponse": 64,
    "SellResponse": 66,
    "FreezeFunctionNotify": 67,
    "ActivateCodeUseResponse": 71,
    "ReLoginResponse": 72,
    "StartGameResponse": 101,
    "GetServerListResponse": 104,
    "RegisterResponse": 106,
    "BindAccountResponse": 108,
    "CreateCharacterResponse": 201,
    "CharacterNotify": 202,
    "HeroNotify": 300,
    "AddHeroNotify": 301,
    "RemoveHeroNotify": 303,
    "UpdateHeroNotify": 304,
    "GetHeroPanelNotify": 305,
    "GetHeroResponse": 321,
    "GetHeroRefreshResponse": 331,
    "HeroStepUpResponse": 335,
    "HeroSoulNotify": 350,
    "AddHeroSoulNotify": 351,
    "UpdateHeroSoulNotify": 352,
    "RemoveHeroSoulNotify": 353,
    "HeroToSoulNotify": 354,
    "HeroRecruitResponse": 356,
    "SetFormationResponse": 401,
    "FormationNotify": 402,
    "AddSocketNotify": 403,
    "SocketNotify": 404,
    "UpdateSocketNotify": 407,
    "SetSocketHeroResponse": 411,
    "SetSocketEquipmentResponse": 413,
    "AlreadyStageNotify": 500,
    "CurrentStageNotify": 501,
    "NewStageNotify": 502,
    "HangNotify": 510,
    "HangResponse": 512,
    "HangCancelResponse": 514,
    "HangSyncResponse": 516,
    "PVEResponse": 601,
    "EliteStageNotify": 650,
    "NewEliteStageNotify": 651,
    "UpdateEliteStageNotify": 652,
    "ElitePVEResponse": 654,
    "EliteStageRemainedTimesNotify": 655,
    "EliteStageResetResponse": 657,
    "EliteStageResetTotalResponse": 659,
    "ActivityStageRemainedTimesNotify": 660,
    "ActivityStageNotify": 661,
    "NewActivityStageNotify": 662,
    "ActivityStagePVEResponse": 664,
    "PlunderNotify": 700,
    "PlunderListResponse": 702,
    "PlunderResponse": 704,
    "PlunderGetRewardResponse": 851,
    "PrisonerReleaseResponse": 853,
    "PrisonerKillResponse": 855,
    "PrisonerListNotify": 705,
    "UpdatePrisonerNotify": 706,
    "NewPrisonerNotify": 707,
    "RemovePrisonerNotify": 708,
    "PrisonerGetResponse": 753,
    "ArenaNotify": 800,
    "ArenaResponse": 802,
    "ArenaPanelResponse": 804,
    "TeamBattleNotify": 900,
    "TeamBattleStartResponse": 904,
    "EquipNotify": 1700,
    "AddEquipNotify": 1701,
    "RemoveEquipNotify": 1702,
    "UpdateEquipNotify": 1703,
    "StrengthEquipResponse": 1705,
    "StepUpEquipResponse": 1771,
    "SpecialEquipmentBuyResponse": 1709,
    "GemNotify": 1750,
    "AddGemNotify": 1751,
    "UpdateGemNotify": 1752,
    "RemoveGemNotify": 1753,
    "MergeGemResponse": 1755,
    "EmbedGemResponse": 1757,
    "UnEmbedGemResponse": 1759,
    "StuffNotify": 1760,
    "AddStuffNotify": 1761,
    "UpdateStuffNotify": 1762,
    "RemoveStuffNotify": 1763,
    "StuffUseResponse": 1765,
    "PrizeNotify": 1800,
    "PrizeResponse": 1802,
    "FriendsNotify": 2000,
    "NewFriendNotify": 2001,
    "RemoveFriendNotify": 2002,
    "UpdateFriendNotify": 2020,
    "FriendsAmountNotify": 2003,
    "PlayerListResponse": 2005,
    "FriendAddResponse": 2007,
    "FriendTerminateResponse": 2009,
    "FriendCancelResponse": 2011,
    "FriendAcceptResponse": 2013,
    "FriendRefuseResponse": 2015,
    "FriendRefreshResponse": 2017,
    "MailNotify": 2100,
    "OpenMailResponse": 2102,
    "DeleteMailResponse": 2104,
    "GetAttachmentResponse": 2106,
    "CheckInNotify": 3000,
    "CheckInUpdateNotify": 3003,
    "CheckInResponse": 3002,
    "TaskNotify": 3100,
    "AchievementNotify": 3200,
    "UpdateAchievementNotify": 3201,
    "StoreNotify": 3300,
    "StorePanelResponse": 3303,
    "StoreBuyResponse": 3305,
    "ChatMessageNotify": 3400,
    "ChatSendResponse": 3402,
    "BroadcastNotify": 3500,
    "GuideNotify": 4000,
    "GuideFinishResponse": 4002,
    "LevyNotify": 4100,
    "LevyResponse": 4102,
    "GetProductsResponse": 4201,
    "BuyVerityResponse": 4203,
    "PurchaseStatusNotify": 4220,
}

REQUEST_TYPE = {
    1: "TestRequest",
    51: "VersionCheckRequest",
    60: "SyncRequest",
    63: "ResumeRequest",
    65: "SellRequest",
    70: "ActivateCodeUseRequest",
    100: "StartGameRequest",
    102: "GetServerListRequest",
    105: "RegisterRequest",
    107: "BindAccountRequest",
    200: "CreateCharacterRequest",
    320: "GetHeroRequest",
    330: "GetHeroRefreshRequest",
    334: "HeroStepUpRequest",
    355: "HeroRecruitRequest",
    400: "SetFormationRequest",
    410: "SetSocketHeroRequest",
    412: "SetSocketEquipmentRequest",
    511: "HangRequest",
    513: "HangCancelRequest",
    515: "HangSyncRequest",
    600: "PVERequest",
    653: "ElitePVERequest",
    656: "EliteStageResetRequest",
    658: "EliteStageResetTotalRequest",
    663: "ActivityStagePVERequest",
    701: "PlunderListRequest",
    703: "PlunderRequest",
    850: "PlunderGetRewardRequest",
    852: "PrisonerReleaseRequest",
    854: "PrisonerKillRequest",
    752: "PrisonerGetRequest",
    801: "ArenaRequest",
    803: "ArenaPanelRequest",
    903: "TeamBattleStartRequest",
    1704: "StrengthEquipRequest",
    1770: "StepUpEquipRequest",
    1708: "SpecialEquipmentBuyRequest",
    1754: "MergeGemRequest",
    1756: "EmbedGemRequest",
    1758: "UnEmbedGemRequest",
    1764: "StuffUseRequest",
    1801: "PrizeRequest",
    2004: "PlayerListRequest",
    2006: "FriendAddRequest",
    2008: "FriendTerminateRequest",
    2010: "FriendCancelRequest",
    2012: "FriendAcceptRequest",
    2014: "FriendRefuseRequest",
    2016: "FriendRefreshRequest",
    2101: "OpenMailRequest",
    2103: "DeleteMailRequest",
    2105: "GetAttachmentRequest",
    3001: "CheckInRequest",
    3302: "StorePanelRequest",
    3304: "StoreBuyRequest",
    3401: "ChatSendRequest",
    4001: "GuideFinishRequest",
    4101: "LevyRequest",
    4200: "GetProductsRequest",
    4202: "BuyVerityRequest",
}

REQUEST_TYPE_REV = {
    "TestRequest": 1,
    "VersionCheckRequest": 51,
    "SyncRequest": 60,
    "ResumeRequest": 63,
    "SellRequest": 65,
    "ActivateCodeUseRequest": 70,
    "StartGameRequest": 100,
    "GetServerListRequest": 102,
    "RegisterRequest": 105,
    "BindAccountRequest": 107,
    "CreateCharacterRequest": 200,
    "GetHeroRequest": 320,
    "GetHeroRefreshRequest": 330,
    "HeroStepUpRequest": 334,
    "HeroRecruitRequest": 355,
    "SetFormationRequest": 400,
    "SetSocketHeroRequest": 410,
    "SetSocketEquipmentRequest": 412,
    "HangRequest": 511,
    "HangCancelRequest": 513,
    "HangSyncRequest": 515,
    "PVERequest": 600,
    "ElitePVERequest": 653,
    "EliteStageResetRequest": 656,
    "EliteStageResetTotalRequest": 658,
    "ActivityStagePVERequest": 663,
    "PlunderListRequest": 701,
    "PlunderRequest": 703,
    "PlunderGetRewardRequest": 850,
    "PrisonerReleaseRequest": 852,
    "PrisonerKillRequest": 854,
    "PrisonerGetRequest": 752,
    "ArenaRequest": 801,
    "ArenaPanelRequest": 803,
    "TeamBattleStartRequest": 903,
    "StrengthEquipRequest": 1704,
    "StepUpEquipRequest": 1770,
    "SpecialEquipmentBuyRequest": 1708,
    "MergeGemRequest": 1754,
    "EmbedGemRequest": 1756,
    "UnEmbedGemRequest": 1758,
    "StuffUseRequest": 1764,
    "PrizeRequest": 1801,
    "PlayerListRequest": 2004,
    "FriendAddRequest": 2006,
    "FriendTerminateRequest": 2008,
    "FriendCancelRequest": 2010,
    "FriendAcceptRequest": 2012,
    "FriendRefuseRequest": 2014,
    "FriendRefreshRequest": 2016,
    "OpenMailRequest": 2101,
    "DeleteMailRequest": 2103,
    "GetAttachmentRequest": 2105,
    "CheckInRequest": 3001,
    "StorePanelRequest": 3302,
    "StoreBuyRequest": 3304,
    "ChatSendRequest": 3401,
    "GuideFinishRequest": 4001,
    "LevyRequest": 4101,
    "GetProductsRequest": 4200,
    "BuyVerityRequest": 4202,
}

TYPE_COMMAND = {
   1: "/test/",
   60: "/sync/",
   63: "/resume/",
   65: "/sell/",
   70: "/activatecode/use/",
   100: "/player/login/",
   102: "/world/server-list/",
   105: "/player/register/",
   107: "/player/bind/",
   200: "/char/create/",
   320: "/hero/get/",
   330: "/heropanel/refresh/",
   334: "/hero/stepup/",
   355: "/hero/recruit/",
   400: "/formation/set/",
   410: "/socket/set/hero/",
   412: "/socket/set/equipment/",
   511: "/hang/",
   513: "/hang/cancel/",
   515: "/hang/sync/",
   600: "/pve/",
   653: "/elitepve/",
   656: "/elite/reset/",
   658: "/elite/reset/total/",
   663: "/activitypve/",
   701: "/plunder/list/",
   703: "/plunder/",
   850: "/plunder/getreward/",
   852: "/prionser/release/",
   854: "/prionser/kill/",
   752: "/prisoner/get/",
   801: "/pvp/",
   803: "/arena/panel/",
   903: "/teambattle/start/",
   1704: "/equip/strengthen/",
   1770: "/equip/stepup/",
   1708: "/equip/specialbuy/",
   1754: "/gem/merge/",
   1756: "/equip/embed/",
   1758: "/equip/unembed/",
   1764: "/stuff/use/",
   1801: "/prize/",
   2004: "/friend/player-list/",
   2006: "/friend/add/",
   2008: "/friend/terminate/",
   2010: "/friend/cancel/",
   2012: "/friend/accept/",
   2014: "/friend/refuse/",
   2016: "/friend/refresh/",
   2101: "/mail/open/",
   2103: "/mail/delete/",
   2105: "/mail/getattachment/",
   3001: "/daily/checkin/",
   3302: "/store/panel/",
   3304: "/store/buy/",
   3401: "/chat/send/",
   4001: "/guide/finish/",
   4101: "/levy/",
   4200: "/purchase/products/",
   4202: "/purchase/verify/",
}

COMMAND_TYPE = {v: k for k, v in TYPE_COMMAND.iteritems()}
COMMAND_REQUEST = {k: REQUEST_TYPE[v] for k, v in COMMAND_TYPE.iteritems()}

