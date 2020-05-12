
from flair.datasets import ColumnCorpus
from flair.data import Sentence
from flair.embeddings import TokenEmbeddings, StackedEmbeddings, WordEmbeddings, CharacterEmbeddings, FlairEmbeddings
from typing import List
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer


def predict(args):
    '''
    Predict the named entities loading an existing model

    Parameters:
    -----------
    args:arguments passed to the parser on CLI
    '''
    # load the model
    model = SequenceTagger.load(args.model_dir + '/final-model.pt')
    # create example sentence
    if(args.predict_file):
        data_dir = args.input_dir + '/data/'
        with open(data_dir + args.predict_file, 'r') as f:
            str_file=f.read()
        sentence = Sentence(str_file)
    else:
        sentence=Sentence("We are looking for data entry operators who live in Bangalore and have a experience in 9 to 5")
    # predict tags and print
    model.predict(sentence)

    print(sentence.to_tagged_string())

if __name__ == "__main__":
    import argparse

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", default=None, type=str, help="Path to input directory")
    parser.add_argument("--model_dir", default=None, type=str, help="Path to model directory")
   # parser.add_argument("--train_file", default=None, type=str, help="Train file")
   # parser.add_argument("--test_file", default=None, type=str, help="Test file")
   # parser.add_argument("--dev_file", default=None, type=str, help="Dev file")
   # parser.add_argument("--flair_model_name_or_path_forward", default="news-forward", type=str, help='Flair forward pretrrained embeddings')
   # parser.add_argument("--flair_model_name_or_path_backward", default="news-backward", type=str, help='Flair backward pretrrained embeddings')
   # parser.add_argument("--character_embeddings", default=True, type=bool, help='Using character embeddings or not')
   # parser.add_argument("--num_train_epochs", default=20, type=int, help="Number of training epochs")
   # parser.add_argument("--per_gpu_batch_size", default=32, type=int, help="batch size for training")
   # parser.add_argument("--train_learning_rate", default=1e-2, type=float, help="Learning rate for training")
   # parser.add_argument("--embeddings_storage_mode", default="gpu", type=str, help="Embeddings storage mode")
   # parser.add_argument("--train_or_predict", default='train', type=str, help="Whether to train or predict. Either use 'train' or 'predict' as argument")
    parser.add_argument("--predict_file", default=None, type=str, help='Predict file, can be mentioned while training too')
    args=parser.parse_args()

predict(args)