import pickle
import os.path as p

from retrieval.base_retrieval import Retrieval


class SparseRetrieval(Retrieval):
    def __init__(self, args):
        super().__init__(args)

        self.name = args.model.retriever_name

        self.embed_path = p.join(args.path.embed, "embedding.bin")
        self.encoder_path = p.join(args.path.embed, f"{self.name}.bin")

    def _exec_embedding(self):
        raise NotImplementedError

    def get_embedding(self):
        if p.isfile(self.embed_path) and p.isfile(self.encoder_path):
            with open(self.embed_path, "rb") as f:
                self.p_embedding = pickle.load(f)

            with open(self.encoder_path, "rb") as f:
                self.encoder = pickle.load(f)
        else:
            self.p_embedding, self.encoder = self._exec_embedding()

    def get_relevant_doc_bulk(self, queries, k=1):
        raise NotImplementedError