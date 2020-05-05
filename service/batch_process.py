from service.storage import Storage
import pickle


def process(body: bytes):
    batch = pickle.loads(body)
    Storage.add_batch_list(batch)
