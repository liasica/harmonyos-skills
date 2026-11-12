---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkweb-access-password-safe
title: 网页接入密码保险箱
breadcrumb: 指南 > 系统 > 安全 > 密码自动填充服务 > 网页接入密码保险箱
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:a89af5dc0d8af8db57adb6aa0ed0454c6ec5994d98d8d4e998bf26ec91d298c0
---

网页中的登录表单，登录成功后，用户可将用户名和密码保存到系统密码保险箱中。再次打开该网页时，密码保险箱可以提供用户名、密码的自动填充。

## 手机使用场景

以下以<https://developer.huawei.com/>网站为例：

1. 在网站中输入用户名、密码，登录成功后，ArkWeb会提示将用户名和密码保存到密码保险箱中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/uwwHz9KvQYuVsYCLsZc2iA/zh-cn_image_0000002815399141.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E758E7E6AAA7566CBD0AEBDFD2F5B22ABC59E8AF06188258F49942A04059C5B)
2. 再次打开相同的网站，点击用户名或者密码框中时，会弹出密码保险箱的填充提示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/f_3JrZ_ATemVsQ5zKho5xw/zh-cn_image_0000002786519566.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=A62A5201B3A35F04FFF651C62A4CC82386283F825B0E5A72291C2FDB4EACE323)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/7CFBRPXJSZ6mrCDNLV0Ujw/zh-cn_image_0000002786359638.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=8CDA609B4E141F4F0E541F18263B2A9F8143BDFFCB95169F858153E4481EA463)
3. 可以选择提示框中的用户名，通过认证，就能直接在网页中填入之前保存的用户名、密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/yL6dksZZSNGSf6UQ-FYpyg/zh-cn_image_0000002815559059.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=2462DEE969F203574ED7C9368A9D205B30058995D868969137AEA0F10D22422E)
4. 点击“使用其他账号”，选择密码保险箱中保存的其他账号。认证后在网页中填入选择的用户名、密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/MpWBt_zfRxWRzlAJcpogJw/zh-cn_image_0000002815399143.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=D653F3C2ABCA27B3C8095CCCA953A85ECEFE44A3013854D68CF9BBC42C9294A9)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/Upi5PNl0RWW-uINl8zVVvA/zh-cn_image_0000002786519568.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=FACD409CB2057DEF5CB1334B4BE7F405ECCE476B461F0A38F0BB10F4047AA53A)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/6huX2ukpQ7aRyylWi-c9pg/zh-cn_image_0000002786359640.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=97CD846614E10370A1E686929D39A6E299E327D212A5E77F05D0BFF94C517148)
5. 点击“手动输入”或者提示框之外的地方，会弹出小艺输入法，会提示可用于密码填充的用户名和钥匙图标。

   点击用户名可触发在网页中填入用户名、密码；点击钥匙图标，进入选择账号的界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/8qXUauwPR4KaaKv45A3ZXA/zh-cn_image_0000002815559061.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=6715175B2E6BD920A3E49B258E1B44992F608A38459CB623CD7E5F49D3CEAEAC)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/9mMOr8ZSRzaGhbN5b1ZukQ/zh-cn_image_0000002815399145.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=48279F29DE3DBEF64D95DC3D5505883FB3127A1688DCC52945ABD3994094D6CC)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/cW8ZtrJKRmiSM9PI6D3CsQ/zh-cn_image_0000002786519570.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=F2308240591392B87AC32B9EF7902FD9CDFD3AE738770AF85746E8707B6C9A93)

## 2in1使用场景

以下以<https://developer.huawei.com/>网站为例：

1. 在网站中输入用户名、密码，登录成功后，ArkWeb会提示将用户名和密码保存到密码保险箱中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/c8rhvybORwylpK67tf3hHQ/zh-cn_image_0000002786359642.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F5F34BE8E12001C2D20CF45584716FC12C98BC2E08EACE777034769CA75A86E)
2. 再次打开相同的网站，点击用户名或者密码框中时，会弹出密码保险箱的下拉框。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/8LPkEhH-ShyCKGVADuistw/zh-cn_image_0000002815559063.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=2CAAC4D8F4CBD9B013D4A5905737C50ABE3E2FB47EF2FBB74504C33F7D97E2D6)
3. 选择下拉框中的用户名，通过认证，就能直接在网页中填入之前保存的用户名、密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/f-W4Sby8SCOpQsAMhmtkeg/zh-cn_image_0000002815399147.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=06AF4D6A95B8F615B3FBEB06BD83510808759AC88AF42404A5C07571F782630B)
4. 也可以点击下拉框中的“使用其他账号”，选择密码保险箱中保存的其他账号。认证后在网页中填入选择的用户名、密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/YmSHmybzQYqtz2J3v18asA/zh-cn_image_0000002786519572.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=6FA916987CDCA7BF45FB02418FC3368149732A6AC60654E4327DFDDF1C5448C6)

## 网页密码保存规格

1、ArkWeb依赖密码表单提交成功后，触发页面跳转到其他页面，才能触发密码保存。

2、Native应用通过ArkWeb实现H5登录，登录成功后请勿立即销毁ArkWeb实例，否则将无法提示密码保存。

## 网页密码表单规格

ArkWeb使用Chromium智能算法，自动识别网页中的用户名、密码元素。算法对用户名、密码表单的设计，有一定的约束。

### 推荐的密码登录表单

1. 使用静态的登录页面或登录表单元素，而不是通过js脚本在页面中动态插入<form>、<input>等表单元素。
2. 用户名密码输入框均使用<input>元素实现，并集成在同一个<form>内，默认可编辑，登录场景有且最多有一个type="password"类型的<input>元素。
3. 点击按钮触发登录，登录成功后，应当触发跳转到新的页面。
4. 用户名框携带autocomplete=“username”，携带id或name属性，并采用如下建议的值，便于算法推断用户名元素：

   ```cpp
   const char* const kUsernameLatin[] = {
       "gatti",      "uzantonomo",   "solonanarana",    "nombredeusuario",
       "olumulo",    "nomenusoris",  "enwdefnyddiwr",   "nomdutilisateur",
       "lolowera",   "notandanafn",  "nomedeusuario",   "vartotojovardas",
       "username",   "ahanjirimara", "gebruikersnaam",  "numedeutilizator",
       "brugernavn", "benotzernumm", "jinalamtumiaji",  "erabiltzaileizena",
       "brukernavn", "benutzername", "sunanmaiamfani",  "foydalanuvchinomi",
       "mosebedisi", "kasutajanimi", "ainmcleachdaidh", "igamalomsebenzisi",
       "nomdusuari", "lomsebenzisi", "jenengpanganggo", "ingoakaiwhakamahi",
       "nomeutente", "namapengguna"};

   const char* const kUserLatin[] = {
       "user",   "wosuta",   "gebruiker",  "utilizator",
       "usor",   "notandi",  "gumagamit",  "vartotojas",
       "fammi",  "olumulo",  "maiamfani",  "cleachdaidh",
       "utent",  "pemakai",  "mpampiasa",  "umsebenzisi",
       "bruger", "usuario",  "panganggo",  "utilisateur",
       "bruker", "benotzer", "uporabnik",  "doutilizador",
       "numake", "benutzer", "covneegsiv", "erabiltzaile",
       "usuari", "kasutaja", "defnyddiwr", "kaiwhakamahi",
       "utente", "korisnik", "mosebedisi", "foydalanuvchi",
       "uzanto", "pengguna", "mushandisi"};

   const char* const kUsernameNonLatin[] = {
    "用户名", "کاتيجونالو", "用戶名", "የተጠቃሚስም",
    "логин", "اسمالمستخدم", "נאמען", "کاصارفکانام",
    "ユーザ名", "όνομα χρήστη", "brûkersnamme", "корисничкоиме",
    "nonitilizatè", "корисничкоиме", "ngaranpamaké", "ຊື່ຜູ້ໃຊ້",
    "användarnamn", "యూజర్పేరు", "korisničkoime", "пайдаланушыаты",
    "שםמשתמש", "ім'якористувача", "کارننوم", "хэрэглэгчийннэр",
    "nomedeusuário", "имяпользователя", "têntruynhập", "பயனர்பெயர்",
    "ainmúsáideora", "ชื่อผู้ใช้", "사용자이름", "імякарыстальніка", "lietotājvārds",
    "потребителскоиме", "uporabniškoime", "колдонуучунунаты", "kullanıcıadı",
    "පරිශීලකනාමය", "istifadəçiadı", "օգտագործողիանունը", "navêbikarhêner", "ಬಳಕೆದಾರಹೆಸರು",
    "emriipërdoruesit", "वापरकर्तानाव", "käyttäjätunnus", "વપરાશકર્તાનામ", "felhasználónév",
    "उपयोगकर्तानाम", "nazwaużytkownika", "ഉപയോക്തൃനാമം", "სახელი", "အသုံးပြုသူအမည်",
    "نامکاربری", "प्रयोगकर्तानाम", "uživatelskéjméno", "ব্যবহারকারীরনাম",
    "užívateľskémeno", "ឈ្មោះអ្នកប្រើប្រាស់"};

   const char* const kUserNonLatin[] = {
    "用户", "użytkownik", "tagatafaʻaaogā", "دکارونکيعکس",
    "用戶", "užívateľ", "корисник", "карыстальнік",
    "brûker", "kullanıcı", "истифода", "អ្នកប្រើ",
    "ọrụ", "ተጠቃሚ", "באַניצער", "хэрэглэгчийн",
    "يوزر", "istifadəçi", "ຜູ້ໃຊ້", "пользователь",
    "صارف", "meahoʻohana", "потребител", "वापरकर्ता",
    "uživatel", "ユーザー", "מִשׁתַמֵשׁ", "ผู้ใช้งาน",
    "사용자", "bikaranîvan", "колдонуучу", "વપરાશકર્તા",
    "përdorues", "ngườidùng", "корисникот", "उपयोगकर्ता",
    "itilizatè", "χρήστης", "користувач", "օգտվողիանձնագիրը",
    "használó", "faoiúsáideoir", "შესახებ", "ব্যবহারকারী",
    "lietotājs", "பயனர்", "ಬಳಕೆದಾರ", "ഉപയോക്താവ്",
    "کاربر", "యూజర్", "පරිශීලක", "प्रयोगकर्ता", "användare",
    "المستعمل", "пайдаланушы", "အသုံးပြုသူကို", "käyttäjä"};

   const char* const kTechnicalWords[] = {
       "uid",         "newtel",     "uaccount",   "regaccount",  "ureg",
       "loginid",     "laddress",   "accountreg", "regid",       "regname",
       "loginname",   "membername", "uname",      "ucreate",     "loginmail",
       "accountname", "umail",      "loginreg",   "accountid",   "loginaccount",
       "ulogin",      "regemail",   "newmobile",  "accountlogin"};

   const char* const kWeakWords[] = {"id", "login", "mail"};
   ```
5. 登录场景，密码框携带autocomplete=“current-password”。
6. 用户名框下面紧挨密码框，中间不要插入其他<input>元素（包括不可见的<input>）。
7. 静态页面中的用户名密码框不可见，则需要确保在静态页面中就存在，而不是跳转页面时插入密码表单。

【案例1】：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/OzIPGmmPQx-AWoOLow98Mw/zh-cn_image_0000002786359644.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=82E5018EE8B4351FC9B124E9BAC6A0206D2CF39591A5F9265C20AE9109ACDAFE)

【案例2】：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/z-9SGuOtRgOa4cmMDr61AA/zh-cn_image_0000002815559065.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC5270B365DFF7AB47BEC983DA6F91D60B0ECD7088FE304D1EE14D26C47F9E57)

### 不支持自动填充的密码登录表单类型

以下场景不会自动弹出账号密码保存提示，如果当前页面存在账号密码保存记录，点击用户名或密码<input>元素仍会触发自动填充弹窗。此时需手动删除已保存的凭据，此后将不再出现自动保存或自动填充弹窗。

1. 初始页面内无用户名密码表单元素，点击登录跳转页面后，新增非<form>类型的用户名密码表单。
2. 用户名输入框type="number"，验证码输入框type="number"，无密码输入框。
3. 页面加载完成，<input>的type属性不是"password"，点击登录才变成"password"类型。
4. 密码<input>元素的autocomplete="one-time-code"或者"cc-\*"。
5. 密码<input>元素在没有autocomplete时，id、name属性上能正则匹配到如下one-time-code或者信用卡标识。

   ```cpp
   inline constexpr char16_t kOneTimePwdRe[] =
       u"one.?time|sms.?(code|token|password|pwd|pass)";

   inline constexpr char16_t kCardCvcRe[] =
       u"verification|card.?identification|security.?code|card.?code"
       u"|security.?value"
       u"|security.?number|card.?pin|c-v-v"
       u"|código de segurança"  // pt-BR
       u"|código de seguridad"  // es-MX
       u"|karten.?prüfn"        // de-DE
       u"|(?:cvn|cvv|cvc|csc|cvd|ccv)"
       // We used to match "cid", but it is a substring of "cidade" (Portuguese for
       // "city") and needs to be handled carefully.
       u"|\\bcid\\b|cccid";
   ```

### 不建议使用的密码登录表单类型

针对期望自动弹出账号密码保存提示的场景，不推荐如下方法，可能存在不符合实现预期的问题。推荐写法见[推荐的密码登录表单](arkweb-access-password-safe.md#推荐的密码登录表单)。

1. 密码输入框携带了autocomplete=“new-password”属性。
2. 用户名和密码元素中间存在其他<input>元素，算法推断出的用户名元素，不符合用户预期。
3. 网页通过JavaScript脚本，变更了<input>元素的焦点或者修改<input>元素的value。
4. 用户名<input>元素上id、name、label内容中匹配到如下密码类型标识：

   ```cpp
   const char* const kNegativeLatin[] = {
       "pin",    "parola",   "wagwoord",   "wachtwoord",
       "fake",   "parole",   "givenname",  "achinsinsi",
       "token",  "parool",   "firstname",  "facalfaire",
       "fname",  "lozinka",  "pasahitza",  "focalfaire",
       "lname",  "passord",  "pasiwedhi",  "iphasiwedi",
       "geslo",  "huahuna",  "passwuert",  "katalaluan",
       "heslo",  "fullname", "phasewete",  "adgangskode",
       "parol",  "optional", "wachtwurd",  "contrasenya",
       "sandi",  "lastname", "cyfrinair",  "contrasinal",
       "senha",  "kupuhipa", "katasandi",  "kalmarsirri",
       "password", "loluszais",  "tenimiafina",
       "second", "passwort", "middlename", "paroladordine",
       "codice", "pasvorto", "familyname", "inomboloyokuvula",
       "modpas", "salasana", "motdepasse", "numeraeleiloaesesi",
       "captcha"};

   const char* const kNegativeNonLatin[] = {
       "fjalëkalim", "የይለፍቃል", "كلمهالسر", "գաղտնաբառ",
       "пароль", "পাসওয়ার্ড", "парола", "密码", "密碼",
       "დაგავიწყდათ", "κωδικόςπρόσβασης", "પાસવર્ડ", "סיסמה",
       "पासवर्ड", "jelszó", "lykilorð", "paswọọdụ",
       "パスワード", "ಪಾಸ್ವರ್ಡ್", "пароль", "ការពាក្យសម្ងាត់",
       "암호", "şîfre", "купуясөз", "ລະຫັດຜ່ານ",
       "slaptažodis", "лозинка", "पासवर्ड", "нууцүг",
       "စကားဝှက်ကို", "पासवर्ड", "رمز", "کلمهعبور",
       "hasło", "пароль", "лозинка", "پاسورڊ",
       "මුරපදය", "contraseña", "lösenord", "гузарвожа",
       "கடவுச்சொல்", "పాస్వర్డ్", "รหัสผ่าน", "пароль",
       "پاسورڈ", "mậtkhẩu", "פּאַראָל", "ọrọigbaniwọle"};
   ```
