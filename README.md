# 使用方法和環境設置

## 影片生成

首先用colab（建議）跑``Adain_video.ipynb``

一開始順著程式格執行，然後在跑到
```
!gdown https://drive.google.com/u/1/uc?id=1Vm7fTGMSZAtS-rOhBXvH-YT7IrgPKupr&export=download
```
的時候因為該檔案是python檔，需要點進output跳出來的連結手動下載`our_test.py`，再把該檔案拉進colab路徑為`/content/Pytorch_Adain_from_scratch`的地方


![](https://i.imgur.com/Mj0e5Me.png)

之後就繼續執行，選擇自己所要的style圖片與目標影片（若要跑兩次風格遷移就在輸入影片的地方放入已經轉移過一次的影片就好）

再來要注意的地方就是在跑到
```
!CUDA_VISIBLE_DEVICES=0 python test.py --content_dir $temp_path --style $pic_name --output $output_path --content_size $min_size_cont --style_size $min_size_styl

%cd /content/pytorch-AdaIN/frames
!for FILE in *; do python3 /content/Pytorch_Adain_from_scratch/our_test.py -c $FILE -s /content/pytorch-AdaIN/photo.jpg --model_state_path /content/Pytorch_Adain_from_scratch/model_state.pth ; done
```
的時候若要使用naoto的model，則把第一行（`!CUDA...`）留著且二三行（`%cd...`和`!for...`）註解掉，而若要使用irasin的model就反過來。
另外可以在`pytorch-AdaIN`下面的`stylized_frames`資料夾試看一下自己有沒有轉成功

最後轉移出來的`out.mp4`會在`pytorch-AdaIN`下面，再自己手動從colab下載就好

以上就是影片生成的操作方法

---

### 圖片生成

Disclosure: 使用的是來自[naoto](https://github.com/naoto0804/pytorch-AdaIN) 以及[irasin](https://github.com/irasin/Pytorch_AdaIN/)的pre-trained model進行修改，與他們github repo的code並無不同，只是修改成可以串接(naoto -> irasin)執行的方式。

使用方法：cd進sub directory ***code*** 再進入 ***two_pass***，並使用以下指令執行。執行結果會放在/code/two_pass/results中。

```shell
python3 run_two_model.py -s [style image path] -c [content image path] -a1 [weight for style in pass 1, default to 1] -a2 [weight for style in pass 2, default to 1]
```

其中，a1, a2應該是介於0~1之間的數，通常(a1, a2) = (1, 1)或(0.8, 1) 能得到不錯的結果

