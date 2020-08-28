from src.config_loader import loadConfig
from src.scraper import scrape
from src.data_writer import saveData

config = loadConfig()
data = scrape(config)
saveData(data)