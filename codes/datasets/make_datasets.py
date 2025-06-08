import sys
import subprocess
import os 

dataset = sys.argv[1]
env = os.environ.copy()
env["CUDA_VISIBLE_DEVICES"] = "3"  # 只使用第0号GPU

print("start_to_get_noise_passages")
subprocess.run(["python", "./get_noise_passages.py", dataset])
print("start_to_get_embedding")
subprocess.run(["python", "./get_embedding.py", dataset], env=env)
print("start_to_classify_docs")
subprocess.run(["python", "./classify_noise_topk.py", dataset])


