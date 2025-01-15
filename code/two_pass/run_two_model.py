import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a1', '--alpha1', help='weight of style for pass 1', type=float)
parser.add_argument('-a2', '--alpha2', help='weight of style for pass 2', type=float)

parser.add_argument('-c', '--content', help='path of content image', type=str)
parser.add_argument('-s', '--style', help='path of style image', type=str)

args = parser.parse_args()

print(f'style:{args.style}, content:{args.content}, a1:{args.alpha1}, a2:{args.alpha2}')

tmp_out_path = "./tmp"
command1 = f"python3 ./models/naoto/test.py --content_size 0 --style_size 0 --content {args.content} --style {args.style} --output {tmp_out_path}"
print(command1)
returned_value = os.system(command1)
command2 = f"python3 ./models/irasin/test.py -c {tmp_out_path}/tmp_result.jpg -s {args.style}"
print(command2)
returned_value = os.system(command2)

os.system("cp ./out.jpg ./results/out.jpg")
os.system("rm out.jpg ./tmp/*.jpg")
