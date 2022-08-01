# [astrobackhacker.tw](https://astrobackhacker.tw/)的原始碼

## 在本地端建立此網站
此個人網站以靜態網站產生器[Lektor](https://www.getlektor.com/)製作，並套用修改[Lektor-Icon Theme](https://github.com/spyder-ide/lektor-icon)。依循下列步驟可在自己的電腦本地端建立此網站：

### 1.安裝Lektor
以pipx安裝Lektor，請參閱[Lektor的安裝文件](https://www.getlektor.com/docs/installation/)。
```bash
pipx install lektor
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