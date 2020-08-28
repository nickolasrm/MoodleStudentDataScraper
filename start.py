from src.config_loader import loadConfig
from src.crawler import crawl
from src.data_writer import saveData

config = loadConfig()
data = crawl(config)
saveData(data)