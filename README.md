# photo
！動作テスト中！
Dropboxのカメラアップロードから写真(jpg)をShotwellが監視するディレクトリへ名前を変えながらコピーする。  

## 前提条件
Ubuntu上でDropboxとShotwellを使用  

## 準備
Shotwell 設定で「ライブラリのディレクトリで新規ファイルを監視する」にチェックを入れてください  
Dropbox カメラアップロードを使用してください  

## インストール
GitHubからクローン  
```
git clone git@github.com:ariichi88/photo.git
```
photo.pyをパスの等っている場所にコピー 
```
cp photo.py /hoge/fuga
```
実行権（パーミッション）の変更 
```
chmod +x photo.py
```

## FromDirとToDirの設定例
FromDir = '/home/username/Dropbox/カメラアップロード/'  
ToDir = '/home/username/Photo/'  

## 使い方
photo.py [日付] 新しい名前  
※　日付はyyyy/mm/ddの形式で、名前は日本語でもOKです。  
※　日付を省略した場合は今日の日付になります。  

## 最後に
Ubuntuを使用していてDropboxとShotwellを使用している人しか関係しませんが良ければ使ってみてください。  
