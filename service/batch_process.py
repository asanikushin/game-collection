from service.storage import Storage
from utils.modelq import BatchList, BatchElement
import pickle


def process(body: bytes):
    batch = pickle.loads(body)
    Storage.add_batch_list(batch)
