# [astrobackhacker.tw](https://astrobackhacker.tw/)的原始碼

## 在本地端建立此網站
此個人網站以靜態網站產生器[Lektor](https://www.getlektor.com/)製作，並套用修改[Lektor-Icon Theme](https://github.com/spyder-ide/lektor-icon)。依循下列步驟可在自己的電腦本地端建立此網站：

### 1.安裝Lektor
1. 安裝Python 3.7版的[Miniconda](https://docs.conda.io/en/latest/miniconda.html)
2. 用conda create指令建立用於此專案的獨立Python開發環境
```bash
# 創建名為LektorEnv的獨立Python開發環境
$ conda create -n LektorEnv python=3.7
```

3. 啟用並進入LektorEnv環境
```bash
$ source activate LektorEnv
```

4. 在LektorEnv環境下用conda install 安裝Lektor
```bash
$ conda install lektor -c conda-forge
```

### 2.下載網站原始碼
```bash
git clone https://github.com/YihaoSu/YihaoSu.github.io.git astrobackhacker.tw
cd astrobackhacker.tw
git submodule update --init --recursive
```

### 3.在本地端啟動網站 http://127.0.0.1:5000
```bash
lektor server
```
關於Lektor的詳細說明，請參閱[Lektor的文件](https://www.getlektor.com/docs/)。