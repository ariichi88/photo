# photo
Dropboxのカメラアップロードから写真(jpg)をShotwellが監視するディレクトリへ名前を変えながらコピーする。  

## pythonのバージョン
3.10.12

## 前提条件
Ubuntu上でDropboxとShotwellを使用  

## 準備
Shotwell 設定で「ライブラリのディレクトリで新規ファイルを監視する」にチェック  
注:現在のShotwellではうまくうごいかない  
Dropbox カメラアップロードを使用  

## 設定
FROM\_DIR = '/home/*username*/Dropbox/カメラアップロード/'  
TO\_DIR = '/home/*username*/Photo/'  

## 実行権（パーミッション）の変更 
```
chmod +x photo.py
```
## 使い方
photo.py [日付] 新しい名前  
※　日付はyyyy/mm/ddの形式で、名前は日本語でもOK  
※　日付を省略した場合は今日の日付  
