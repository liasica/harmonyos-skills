---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkweb-access-password-safe
title: 网页接入密码保险箱
breadcrumb: 指南 > 系统 > 安全 > 密码自动填充服务 > 网页接入密码保险箱
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:92da12774bd4be75b43e300574a7938301338dc33d12f1a2232980af9d16dfce
---

网页中的登录表单，登录成功后，用户可将用户名和密码保存到系统密码保险箱中。再次打开该网页时，密码保险箱可以提供用户名、密码的自动填充。

## 手机使用场景

以下以<https://developer.huawei.com/>网站为例：

1. 在网站中输入用户名、密码，登录成功后，ArkWeb会提示将用户名和密码保存到密码保险箱中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/ODDsfhODTmWnnebk8mHcsQ/zh-cn_image_0000002552798716.png?HW-CC-KV=V1&HW-CC-Date=20260427T234208Z&HW-CC-Expire=86400&HW-CC-Sign=9E6241813BC5B2EEA346A1E2E7EB7CC63EE325A3F64A45E05BA2081BC148EA9A)
2. 再次打开相同的网站，点击用户名或者密码框中时，会弹出密码保险箱的填充提示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/TzWI3ZPpRuKLCGwGeQDnCg/zh-cn_image_0000002583438411.png?HW-CC-KV=V1&HW-CC-Date=20260427T234208Z&HW-CC-Expire=86400&HW-CC-Sign=F16ECC3D21FC6953E73F246E6CB4F435CAF890440EB7D63C4FE480F06B80AF6A)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/evL6GRw3TRiIvqpLWAH41Q/zh-cn_image_0000002552958366.png?HW-CC-KV=V1&HW-CC-Date=20260427T234208Z&HW-CC-Expire=86400&HW-CC-Sign=04420854301EDD935FBF77A490AF1D0342E9E9B8CEA1E2424B63018AFA8EAAF0)
3. 可以选择提示框中的用户名，通过认证，就能直接在网页中填入之前保存的用户名、密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/grL4KM-DSCeJ01ZZrrMEiw/zh-cn_image_0000002583478367.png?HW-CC-KV=V1&HW-CC-Date=20260427T234208Z&HW-CC-Expire=86400&HW-CC-Sign=AC45A1CA7047112B00F2B3869D8D57CC2106A686F0B3178EC3828FC5C27DBCB5)
4. 点击“使用其他账号”，选择密码保险箱中保存的其他账号。认证后在网页中填入选择的用户名、密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/JGpqf1qHQg6Oy6L25k6-tw/zh-cn_image_0000002552798718.png?HW-CC-KV=V1&HW-CC-Date=20260427T234208Z&HW-CC-Expire=86400&HW-CC-Sign=CDE73D6B6A69455ACC4F48C42CCAA8D9E31F5CD5C4873E954AD7AED3BA877927)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/5CNARFtURMmtRFAiuiNNHw/zh-cn_image_0000002583438413.png?HW-CC-KV=V1&HW-CC-Date=20260427T234208Z&HW-CC-Expire=86400&HW-CC-Sign=DC671B0C96D35EAE1EAA13C7C5F26DBF071D66565D408C0B0E780C80EAC96578)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/aQeXexwJSwWRgAbGN9_iZw/zh-cn_image_0000002552958368.png?HW-CC-KV=V1&HW-CC-Date=20260427T234208Z&HW-CC-Expire=86400&HW-CC-Sign=4457A85959B3B177DBC0A85777F3E6151A3280E62D2B7EE2C9DFF0BD8B810C34)
5. 点击“手动输入”或者提示框之外的地方，会弹出小艺输入法，会提示可用于密码填充的用户名和钥匙图标。

   点击用户名可触发在网页中填入用户名、密码；点击钥匙图标，进入选择账号的界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/M0Ku7bsnSC6xwJaAUPx-3A/zh-cn_image_0000002583478369.png?HW-CC-KV=V1&HW-CC-Date=20260427T234208Z&HW-CC-Expire=86400&HW-CC-Sign=868898393527A6623F11CEF7275471A84AB128207A1D33AEDB851340526DAC2C)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/J5cPOpFZSkaRbQKXqzJyqQ/zh-cn_image_0000002552798720.png?HW-CC-KV=V1&HW-CC-Date=20260427T234208Z&HW-CC-Expire=86400&HW-CC-Sign=A1995415B2E7177373FD3D7B979CFCAA7B6F1386029BF382BC7FA5AA1BD4EDAE)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/W9zfphljQB-87J3I_bZWjA/zh-cn_image_0000002583438415.png?HW-CC-KV=V1&HW-CC-Date=20260427T234208Z&HW-CC-Expire=86400&HW-CC-Sign=B28F7BD8569EB8BC67C6B940A93CD8AC8FFC8BE9A781F096337B66F9710C4153)

## 2in1使用场景

以下以<https://developer.huawei.com/>网站为例：

1. 在网站中输入用户名、密码，登陆成功后，ArkWeb会提示将用户名和密码保存到密码保险箱中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/kuV2hcGvQpy-l9MhlvjKxg/zh-cn_image_0000002552958370.png?HW-CC-KV=V1&HW-CC-Date=20260427T234208Z&HW-CC-Expire=86400&HW-CC-Sign=CC78C812C0CEE2AEBCD236900D90D47911D7255519F67B54A1104B195F73F0CE)
2. 再次打开相同的网站，点击用户名或者密码框中时，会弹出密码保险箱的下拉框。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/P7b0K7V-TdCnHqk5kwjucQ/zh-cn_image_0000002583478371.png?HW-CC-KV=V1&HW-CC-Date=20260427T234208Z&HW-CC-Expire=86400&HW-CC-Sign=C85E8D24DBDBC434C9BDBFDE491815D12A0E3C687A1654D05AE5E9A050B8C2A8)
3. 选择下拉框中的用户名，通过认证，就能直接在网页中填入之前保存的用户名、密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/Y4oR0lp1RgurhfMMk4IgAA/zh-cn_image_0000002552798722.png?HW-CC-KV=V1&HW-CC-Date=20260427T234208Z&HW-CC-Expire=86400&HW-CC-Sign=48D1358906DAD0E0061C1D2CF851C8401DEDD8C449268802679A07AC4D5D132D)
4. 也可以点击下拉框中的“使用其他账号”，选择密码保险箱中保存的其他账号。认证后在网页中填入选择的用户名、密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/TaX_a2XqSka-o_tI6hZBEA/zh-cn_image_0000002583438417.png?HW-CC-KV=V1&HW-CC-Date=20260427T234208Z&HW-CC-Expire=86400&HW-CC-Sign=CA77AB5FDF02C6D5A298D98F78A58893BA895E5BF36DCBD508840EA6C4F3A92E)

## 网页密码保存规格

1、ArkWeb依赖密码表单提交成功后，触发页面跳转到其他页面，才能触发密码保存。

2、Native应用通过ArkWeb实现H5登入，登录成功后请勿立即销毁ArkWeb实例，否则将无法提示密码保存。

## 网页密码表单规格

ArkWeb使用Chromium智能算法，自动识别网页中的用户名、密码元素。算法对用户名、密码表单的设计，有一定的约束。

### 推荐的密码登录表单

1. 使用静态的登录页面或登录表单元素，而不是通过js脚本在页面中动态插入<form>、<input>等表单元素。
2. 用户名密码输入框均使用<input>元素实现，并集成在同一个<form>内，默认可编辑，登录场景有且最多有一个type="password"类型的<input>元素。
3. 点击按钮触发登录，登录成功后，应当触发跳转到新的页面。
4. 用户名框携带autocomplete=“username”，携带id或name属性，并采用如下建议的值，便于算法推断用户名元素：

   ```
   1. const char* const kUsernameLatin[] = {
   2. "gatti",      "uzantonomo",   "solonanarana",    "nombredeusuario",
   3. "olumulo",    "nomenusoris",  "enwdefnyddiwr",   "nomdutilisateur",
   4. "lolowera",   "notandanafn",  "nomedeusuario",   "vartotojovardas",
   5. "username",   "ahanjirimara", "gebruikersnaam",  "numedeutilizator",
   6. "brugernavn", "benotzernumm", "jinalamtumiaji",  "erabiltzaileizena",
   7. "brukernavn", "benutzername", "sunanmaiamfani",  "foydalanuvchinomi",
   8. "mosebedisi", "kasutajanimi", "ainmcleachdaidh", "igamalomsebenzisi",
   9. "nomdusuari", "lomsebenzisi", "jenengpanganggo", "ingoakaiwhakamahi",
   10. "nomeutente", "namapengguna"};

   12. const char* const kUserLatin[] = {
   13. "user",   "wosuta",   "gebruiker",  "utilizator",
   14. "usor",   "notandi",  "gumagamit",  "vartotojas",
   15. "fammi",  "olumulo",  "maiamfani",  "cleachdaidh",
   16. "utent",  "pemakai",  "mpampiasa",  "umsebenzisi",
   17. "bruger", "usuario",  "panganggo",  "utilisateur",
   18. "bruker", "benotzer", "uporabnik",  "doutilizador",
   19. "numake", "benutzer", "covneegsiv", "erabiltzaile",
   20. "usuari", "kasutaja", "defnyddiwr", "kaiwhakamahi",
   21. "utente", "korisnik", "mosebedisi", "foydalanuvchi",
   22. "uzanto", "pengguna", "mushandisi"};

   24. const char* const kUsernameNonLatin[] = {
   25. "用户名", "کاتيجونالو", "用戶名", "የተጠቃሚስም",
   26. "логин", "اسمالمستخدم", "נאמען", "کاصارفکانام",
   27. "ユーザ名", "όνομα χρήστη", "brûkersnamme", "корисничкоиме",
   28. "nonitilizatè", "корисничкоиме", "ngaranpamaké", "ຊື່ຜູ້ໃຊ້",
   29. "användarnamn", "యూజర్పేరు", "korisničkoime", "пайдаланушыаты",
   30. "שםמשתמש", "ім'якористувача", "کارننوم", "хэрэглэгчийннэр",
   31. "nomedeusuário", "имяпользователя", "têntruynhập", "பயனர்பெயர்",
   32. "ainmúsáideora", "ชื่อผู้ใช้", "사용자이름", "імякарыстальніка", "lietotājvārds",
   33. "потребителскоиме", "uporabniškoime", "колдонуучунунаты", "kullanıcıadı",
   34. "පරිශීලකනාමය", "istifadəçiadı", "օգտագործողիանունը", "navêbikarhêner", "ಬಳಕೆದಾರಹೆಸರು",
   35. "emriipërdoruesit", "वापरकर्तानाव", "käyttäjätunnus", "વપરાશકર્તાનામ", "felhasználónév",
   36. "उपयोगकर्तानाम", "nazwaużytkownika", "ഉപയോക്തൃനാമം", "სახელი", "အသုံးပြုသူအမည်",
   37. "نامکاربری", "प्रयोगकर्तानाम", "uživatelskéjméno", "ব্যবহারকারীরনাম",
   38. "užívateľskémeno", "ឈ្មោះអ្នកប្រើប្រាស់"};

   40. const char* const kUserNonLatin[] = {
   41. "用户", "użytkownik", "tagatafaʻaaogā", "دکارونکيعکس",
   42. "用戶", "užívateľ", "корисник", "карыстальнік",
   43. "brûker", "kullanıcı", "истифода", "អ្នកប្រើ",
   44. "ọrụ", "ተጠቃሚ", "באַניצער", "хэрэглэгчийн",
   45. "يوزر", "istifadəçi", "ຜູ້ໃຊ້", "пользователь",
   46. "صارف", "meahoʻohana", "потребител", "वापरकर्ता",
   47. "uživatel", "ユーザー", "מִשׁתַמֵשׁ", "ผู้ใช้งาน",
   48. "사용자", "bikaranîvan", "колдонуучу", "વપરાશકર્તા",
   49. "përdorues", "ngườidùng", "корисникот", "उपयोगकर्ता",
   50. "itilizatè", "χρήστης", "користувач", "օգտվողիանձնագիրը",
   51. "használó", "faoiúsáideoir", "შესახებ", "ব্যবহারকারী",
   52. "lietotājs", "பயனர்", "ಬಳಕೆದಾರ", "ഉപയോക്താവ്",
   53. "کاربر", "యూజర్", "පරිශීලක", "प्रयोगकर्ता", "användare",
   54. "المستعمل", "пайдаланушы", "အသုံးပြုသူကို", "käyttäjä"};

   56. const char* const kTechnicalWords[] = {
   57. "uid",         "newtel",     "uaccount",   "regaccount",  "ureg",
   58. "loginid",     "laddress",   "accountreg", "regid",       "regname",
   59. "loginname",   "membername", "uname",      "ucreate",     "loginmail",
   60. "accountname", "umail",      "loginreg",   "accountid",   "loginaccount",
   61. "ulogin",      "regemail",   "newmobile",  "accountlogin"};

   63. const char* const kWeakWords[] = {"id", "login", "mail"};
   ```
5. 登录场景，密码框携带autocomplete=“current-password”。
6. 用户名框下面紧挨密码框，中间不要插入其他<input>元素（包括不可见的<input>）。
7. 静态页面中的用户名密码框不可见，则需要确保在静态页面中就存在，而不是跳转页面时插入密码表单。

【案例1】：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/EMaa6zeOSYaWjbn7BcAo7Q/zh-cn_image_0000002552958372.png?HW-CC-KV=V1&HW-CC-Date=20260427T234208Z&HW-CC-Expire=86400&HW-CC-Sign=876BA692E0B784C7F9BF5879D9F3C960AF8679B7387D12D39FAFC366DD6973F3)

【案例2】：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/jbcE-eC0RuuwKKrurhj9Tw/zh-cn_image_0000002583478373.png?HW-CC-KV=V1&HW-CC-Date=20260427T234208Z&HW-CC-Expire=86400&HW-CC-Sign=211947A4737224E0D74FC7A34BB320B091683D99A9E4A183E559ABF222AA7E63)

### 不支持自动填充的密码登录表单类型

1. 初始页面内无用户名密码表单元素，点击登录跳转页面后，新增非<form>类型的用户名密码表单。
2. 密码输入框携带了autocomplete=“new-password”属性。
3. 用户名输入框type="number"，验证码输入框type="number"，无密码输入框。
4. 用户名和密码元素中间存在其他<input>元素，算法推断出的用户名元素，不符合用户预期。
5. 网页通过javascript脚本，变更了<input>元素的焦点或者修改<input>元素的value。
6. 用户名<input>元素上id、name、label内容中匹配到如下密码类型标识：

   ```
   1. const char* const kNegativeLatin[] = {
   2. "pin",    "parola",   "wagwoord",   "wachtwoord",
   3. "fake",   "parole",   "givenname",  "achinsinsi",
   4. "token",  "parool",   "firstname",  "facalfaire",
   5. "fname",  "lozinka",  "pasahitza",  "focalfaire",
   6. "lname",  "passord",  "pasiwedhi",  "iphasiwedi",
   7. "geslo",  "huahuna",  "passwuert",  "katalaluan",
   8. "heslo",  "fullname", "phasewete",  "adgangskode",
   9. "parol",  "optional", "wachtwurd",  "contrasenya",
   10. "sandi",  "lastname", "cyfrinair",  "contrasinal",
   11. "senha",  "kupuhipa", "katasandi",  "kalmarsirri",
   12. "password", "loluszais",  "tenimiafina",
   13. "second", "passwort", "middlename", "paroladordine",
   14. "codice", "pasvorto", "familyname", "inomboloyokuvula",
   15. "modpas", "salasana", "motdepasse", "numeraeleiloaesesi",
   16. "captcha"};

   18. const char* const kNegativeNonLatin[] = {
   19. "fjalëkalim", "የይለፍቃል", "كلمهالسر", "գաղտնաբառ",
   20. "пароль", "পাসওয়ার্ড", "парола", "密码", "密碼",
   21. "დაგავიწყდათ", "κωδικόςπρόσβασης", "પાસવર્ડ", "סיסמה",
   22. "पासवर्ड", "jelszó", "lykilorð", "paswọọdụ",
   23. "パスワード", "ಪಾಸ್ವರ್ಡ್", "пароль", "ការពាក្យសម្ងាត់",
   24. "암호", "şîfre", "купуясөз", "ລະຫັດຜ່ານ",
   25. "slaptažodis", "лозинка", "पासवर्ड", "нууцүг",
   26. "စကားဝှက်ကို", "पासवर्ड", "رمز", "کلمهعبور",
   27. "hasło", "пароль", "лозинка", "پاسورڊ",
   28. "මුරපදය", "contraseña", "lösenord", "гузарвожа",
   29. "கடவுச்சொல்", "పాస్వర్డ్", "รหัสผ่าน", "пароль",
   30. "پاسورڈ", "mậtkhẩu", "פּאַראָל", "ọrọigbaniwọle"};
   ```
7. 用户名<input>元素的autocomplete="one-time-code"或者"cc-\*"，或者id、name属性上能正则匹配到如下one-time-code或者信用卡标识：

   ```
   1. inline constexpr char16_t kOneTimePwdRe[] =
   2. u"one.?time|sms.?(code|token|password|pwd|pass)";

   4. inline constexpr char16_t kCardCvcRe[] =
   5. u"verification|card.?identification|security.?code|card.?code"
   6. u"|security.?value"
   7. u"|security.?number|card.?pin|c-v-v"
   8. u"|código de segurança"  // pt-BR
   9. u"|código de seguridad"  // es-MX
   10. u"|karten.?prüfn"        // de-DE
   11. u"|(?:cvn|cvv|cvc|csc|cvd|ccv)"
   12. // We used to match "cid", but it is a substring of "cidade" (Portuguese for
   13. // "city") and needs to be handled carefully.
   14. u"|\\bcid\\b|cccid";
   ```
8. 页面加载完成，<input>的type属性不是"password"，点击登录才变成"password"类型。
