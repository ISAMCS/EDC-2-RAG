import sys
import subprocess
eval_model = sys.argv[1]#llama3_request, GPT_Instruct_request, ChatGPT_request
date = sys.argv[2]
dataset = sys.argv[3]#400 or 113
topkk = sys.argv[4] # "[20, 50, 70]"
noises = sys.argv[5] # "[20 ,60, 80]"
benchmark = sys.argv[6]
#python run_baseline_rag.py qwen 0518 full "[5,10,20,30,50,70,100]" "[0]" twowiki

print("start_to_run")
print("start_to_eval")
subprocess.run(["python", "../run_methods/eval_baseline_rag.py", eval_model, date, dataset,topkk,noises,benchmark])
print("end_eval")
print("start_to_extract_answer")
if eval_model == "GPT_Instruct_request":
    eval_method = "eval_3.5instruct"
elif eval_model == "ChatGPT_request":
    eval_method = "eval_3.5turbo"
elif eval_model == "GPT4o_request":
    eval_method = "eval_4o"
elif eval_model == "GPT4omini_request":
    eval_method = "eval_4omini"
etype = "rag" ## rag or ours
subprocess.run(["python", "../eval_metric/extracted_answer_topkk.py", date, dataset, eval_method, etype,topkk,noises,benchmark])
print("end_extracte_answer")
print("start_to_caculate_F1_EM")   
subprocess.run(["python", "../eval_metric/caculate_F1_EM.py", date, dataset, eval_method, etype,topkk,noises,benchmark])
print("end_caculate_F1_EM")