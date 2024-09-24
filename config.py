# experiment ID
import spacy

exp = "exp-1"

# data directories
data_dir = "/mnt/hdd/karmpatel/naman/demo/squad"
train_dir = data_dir + "/train"
dev_dir = data_dir + "/dev"

# model paths
spacy_en = spacy.load('en_core_web_sm')
glove = "/mnt/hdd/karmpatel/naman/demo/glove/" + "glove.6B.{}d.txt"
squad_models = "/raid/home/namanmalpani/final_yr/question_answering/output/" + exp

# preprocessing values
max_words = -1
word_embedding_size = 100
char_embedding_size = 8
max_len_context = 400
max_len_question = 50
max_len_word = 25

# training hyper-parameters
num_epochs = 3
batch_size = 64
learning_rate = 0.5
drop_prob = 0.2
hidden_size = 100
char_channel_width = 5
char_channel_size = 100
cuda = True
pretrained = False
