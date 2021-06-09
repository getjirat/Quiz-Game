import pickle
def _init_():
  question_lists = ["",""]
  answer_lists = ["",""]
  question_lists = pickle.load(open("assets/data/question-lists.txt","rb"))
  answer_lists = pickle.load(open("assets/data/answer-lists.txt","rb"))
  print(question_lists)
  print(answer_lists)
_init_()
input("Press Key [ENTER] to Continue.")
  
