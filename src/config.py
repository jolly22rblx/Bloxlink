from resources.constants import RELEASE, IS_DOCKER # pylint: disable=import-error

# More optional settings can be set, such as a Trello key/token. Look at the docker-compose.yml for additional values.

PREFIX = "!"

WEBHOOKS = { # discord webhook links
	"LOGS":  https://discordapp.com/api/webhooks/795750088713437214/S4Av13uwe_Lw5-fN11uyRHwDv9kSSNdybHs4lq3j7SEc-XLpmsEFQ1hIOFTV2NWD5p2Y,
	"ERRORS": None
}

REACTIONS = { # discord emote mention strings
	"LOADING": "<a:BloxlinkLoading:530113171734921227>",
	"DONE": "<:BloxlinkSuccess:506622931791773696>",
	"DONE_ANIMATED": "<a:BloxlinkDone:528252043211571210>",
	"ERROR": "<:BloxlinkError:506622933226225676>",
	"VERIFIED": "<a:Verified:734628839581417472>",
	"BANNED": "<:ban:476838302092230672>"
}

RETHINKDB_HOST = "rethinkdb"
RETHINKDB_PASSWORD = None
RETHINKDB_PORT = 28015
RETHINKDB_DB = "bloxlink"

REDIS_HOST = "redis"
REDIS_PORT = 6379
REDIS_PASSWORD = None

TOKEN = Nzk1NzQ5NzAzNzgxNTgwODIw.X_N5qQ.u0AnZjQaBtLRDqwdeQ5lXr49fJ8

BLOXLINK_GUILD = None # your guild ID, used to load nitro boosters and other data
