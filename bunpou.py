## １ 変数の使い方
# 変数を使って、「ねずこ」と「ぜんいつ」 は仲間ですとprint文を使って表示させてみようなお、ねずこをname1、ぜんいつをname2として定義してください。
name1 = 'ねずこ'
name2 = 'ぜんいつ'
print(name1 + 'と' + name2 + 'は仲間です')

## ２ if文の使い方
#１のソースを改造して、name2が敵キャラの「むざん」だった場合に仲間ではありませんと表示させてみよう。
name2 = 'むざん'
if name2 == 'むざん':
   print('仲間ではありません')

## ３ 配列の使い方
#以下の配列に対して、キャラクター「ぜんいつ」を追加してみよう。
#appendを使うことで追加できます。
name=["たんじろう","ぎゆう","ねずこ","むざん"]
name.append('ぜんいつ') 
print(name)

## ４ for文の使い方
#３のソースコードで使用したnameのキャラクターをfor文を使って、１行に１キャラクター表示してみよう
for cal in name:
    print(cal)


## ５　関数の使い方
#いままで作ったソースコードを全て関数化してみよう。
#関数化したら、関数を呼び出して結果が表示されることを確認してみよう。

def nakama_hyouji():
    name1 = 'ねずこ'
    name2 = 'ぜんいつ'
    print(name1 + 'と' + name2 + 'は仲間です')

nakama_hyouji()    

def not_nakama():
   name2 = 'むざん'
   if name2 == 'むざん':
      print('仲間ではありません')

not_nakama()

def hairetu_def():
    name=["たんじろう","ぎゆう","ねずこ","むざん"]
    name.append('ぜんいつ') 
    print(name)

hairetu_def()

def forbun_def():
    for cal in name:
        print(cal)

forbun_def()


## ６ 引数を使う関数の使い方
#以下のようにhikisuuの部分が引数です。引数は関数の外から変数を関数内に渡すことができます。
#このような引数を使う関数を作成してみよう。
def namae_kensaku(cal_mei):
    name = ["たんじろう","ぎゆう","ねずこ","むざん"]
    for cal in name:
        if cal_mei == cal: 
           print(cal_mei + 'は含まれます。')
        else:
           print(cal_mei + 'は含まれません。') 
        break

namae_kensaku('ぜんいつ')


