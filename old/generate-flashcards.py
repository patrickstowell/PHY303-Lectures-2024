import json
import sys

for i in [10]:
  unit = "unit" + str(i+1)

  with open(f"{unit}/phy303-{unit}-quiz-answers.json") as f:
    d = json.load(f)

    answers = []

    for v in d:
      result = None
      question = v["question"]
      for a in v["answers"]:
        if a["correct"]: result = a["answer"]

      answers.append({
        'front': question,
        'back': result
      })


    with open(f"{unit}/phy303-{unit}-flashcard-answers.json", "w") as answers_data_file:
      json.dump(answers, answers_data_file, indent=4, sort_keys=True)

    print(unit + " DONE")
