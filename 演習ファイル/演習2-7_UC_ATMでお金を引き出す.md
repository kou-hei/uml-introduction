### ユースケース図
ATMで「お金を引き出す」
### 概略
銀行のATMを利用して、自分の口座からキャッシュカードで必要なお金を引き出します。
### アクター
利用者
### 事前条件
アクターが口座とキャッシュカードを持っていること。

### 事後条件
アクターの口座から指定された金額が引き出されること。

### 基本フロー
1.顧客は、ATMにキャッシュカードを挿入する。
2.ATMは、キャッシュカードの情報を読み取り、顧客に暗証番号を入力するように促す。
3.顧客は、ATMの画面に表示されたキーパッドを使って、自身の暗証番号を入力する。
4.ATMは、暗証番号が正しいかどうかを確認する。
5.暗証番号が正しい場合、ATMは、顧客に現金引き出しのオプションを提供する。
6.顧客は、引き出したい金額を指定する。
7.ATMは、顧客の口座から指定された金額を引き出し、現金を顧客に提供する。
8.顧客は、ATMからキャッシュカードを取り出し完了したことを確認する。

### 代替フロー
4-1.暗証番号が正しくない場合、ATMは、顧客に再試行するように促す。
4-2.引き出したい金額が残高を超えている場合、ATMは、顧客に引き出せる最大額を示し、顧客に再試行するように促す。

### 例外フロー

### ユースケース名
[基本シナリオ]
1.顧客は、ATMにキャッシュカードを挿入する。
2.ATMは、キャッシュカードの情報を読み取り、顧客に暗証番号を入力するように促す。
3.顧客は、ATMの画面に表示されたキーパッドを使って、自身の暗証番号を入力する。
4.ATMは、暗証番号が正しいかどうかを確認する。
5.暗証番号が正しい場合、ATMは、顧客に現金引き出しのオプションを提供する。
6.顧客は、引き出したい金額を指定する。
7.ATMは、顧客の口座から指定された金額を引き出し、現金を顧客に提供する。
8.顧客は、ATMからキャッシュカードを取り出し完了したことを確認する。

### 例外シナリオ
