from .Antispam import SpamDetectionGenerator, SpamManager
from .Ban import BanManager
from .Base import CogManager, questionnaire
from .Birthday import BirthdayManager
from .CommandHinter import CommandHinter, CommandResponseGenerator
from .Convertors import TimeConvertor
from .Database import DatabaseManager, create_mysql
from .Economy import EconomyManager, EconomyAccount
from .FiveM import FiveMServer
from .Imaging import ImageManager, Backgrounds
from .Infractions import InfractionManager
from .Interactions.Interaction import Interaction, OptionType
from .Interactions.client import SlashManager
from .InviteTracker import InviteTracker
from .Kick import KickManager
from .Levelling import LevellingManager
from .MessageFilter import MessageFilter, MessageResponseGenerator
from .Music import *
from .Mute import MuteManager, AlreadyMuted
from .Paginator import PageManager, generate_embeds, ButtonsPageManager
from .Prefix import PrefixManager
from .Punishments import Punishment
from .ReactionRoles import ReactionManager
from .Spotify import SpotifyClient
from .Template import TemplateManager

__title__ = "discordSuperUtils"
__version__ = "0.1.7"
__author__ = "Koyashie07 & Adam7100"
__license__ = "MIT"
