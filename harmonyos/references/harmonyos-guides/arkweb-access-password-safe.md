---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkweb-access-password-safe
title: 网页接入密码保险箱
breadcrumb: 指南 > 系统 > 安全 > 密码自动填充服务 > 网页接入密码保险箱
category: harmonyos-guides
scraped_at: 2026-04-29T13:30:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b1c103458b0bf101926f523203e4aba374ee61cd45052572fd66c7fe7130e445
---

网页中的登录表单，登录成功后，用户可将用户名和密码保存到系统密码保险箱中。再次打开该网页时，密码保险箱可以提供用户名、密码的自动填充。

## 手机使用场景

以下以<https://developer.huawei.com/>网站为例：

1. 在网站中输入用户名、密码，登录成功后，ArkWeb会提示将用户名和密码保存到密码保险箱中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/dSQr6KvPSQKa8O93Qja4kQ/zh-cn_image_0000002558764864.png?HW-CC-KV=V1&HW-CC-Date=20260429T053040Z&HW-CC-Expire=86400&HW-CC-Sign=3DF596E152A62442FB0CA2BACF26A0E001A1E15DAB3ABF59D1C7DB17529E3FFB)
2. 再次打开相同的网站，点击用户名或者密码框中时，会弹出密码保险箱的填充提示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/DbD5nk_PR3-vD75V9_XI2A/zh-cn_image_0000002558605208.png?HW-CC-KV=V1&HW-CC-Date=20260429T053040Z&HW-CC-Expire=86400&HW-CC-Sign=BB389EAEAD7A323A6DA3BB78440E7BCC9486E31412C90F26A148A9798ECDD135)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/ppdvjRcITJ6MBNcdWohQMg/zh-cn_image_0000002589324733.png?HW-CC-KV=V1&HW-CC-Date=20260429T053040Z&HW-CC-Expire=86400&HW-CC-Sign=6B8742494ACA621390C98101B2BB31D42BE5AC1DB566677B20D6DDBC312007E7)
3. 可以选择提示框中的用户名，通过认证，就能直接在网页中填入之前保存的用户名、密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/cOQX2az1R1a7Vn-_wplvjQ/zh-cn_image_0000002589244671.png?HW-CC-KV=V1&HW-CC-Date=20260429T053040Z&HW-CC-Expire=86400&HW-CC-Sign=274D648C0B78502B4A6FF8358D61A55D2EE26043C73FACDCB15FDE31B3EA354E)
4. 点击“使用其他账号”，选择密码保险箱中保存的其他账号。认证后在网页中填入选择的用户名、密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/uztaVQAdRWS8xXDkDP083Q/zh-cn_image_0000002558764866.png?HW-CC-KV=V1&HW-CC-Date=20260429T053040Z&HW-CC-Expire=86400&HW-CC-Sign=FDEF3320A2C4490E12FB49182B7D62B489615F1C7722295C0F1B4655413A4A98)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/TUp2BZjER-qijOJbXfz0TQ/zh-cn_image_0000002558605210.png?HW-CC-KV=V1&HW-CC-Date=20260429T053040Z&HW-CC-Expire=86400&HW-CC-Sign=86A2CED42FDA778EFCF22EB080BD42124A6344E81642689E7B51AAB89E81AA85)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/AVQZokAeR_KLGqGibWcZhg/zh-cn_image_0000002589324735.png?HW-CC-KV=V1&HW-CC-Date=20260429T053040Z&HW-CC-Expire=86400&HW-CC-Sign=EF32878C08432091D6886F3DD07EA974683D08E36D06E08D1B677C8F53AD45FE)
5. 点击“手动输入”或者提示框之外的地方，会弹出小艺输入法，会提示可用于密码填充的用户名和钥匙图标。

   点击用户名可触发在网页中填入用户名、密码；点击钥匙图标，进入选择账号的界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/FKn3_NjXS9yMqQOVB6biSw/zh-cn_image_0000002589244673.png?HW-CC-KV=V1&HW-CC-Date=20260429T053040Z&HW-CC-Expire=86400&HW-CC-Sign=81A97F914858C2F91CC9A216333C1C06C17E8ED866C8AC903AD4083F41065888)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/Ae_uUFTnSiaDCU6E9gUu8w/zh-cn_image_0000002558764868.png?HW-CC-KV=V1&HW-CC-Date=20260429T053040Z&HW-CC-Expire=86400&HW-CC-Sign=0A75F1967667DD5B189403B481FE00B772D9534608CBB1D2FF9C5AD21C33A6BD)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/02nXiZcDRlileCc1LR6dbw/zh-cn_image_0000002558605212.png?HW-CC-KV=V1&HW-CC-Date=20260429T053040Z&HW-CC-Expire=86400&HW-CC-Sign=83CE5A913A96ED82DFC9196A1B822CB16807F3DE27136AF964556B8CCAE64803)

## 2in1使用场景

以下以<https://developer.huawei.com/>网站为例：

1. 在网站中输入用户名、密码，登陆成功后，ArkWeb会提示将用户名和密码保存到密码保险箱中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/mv60o6X2RkyUq0_nThrIUA/zh-cn_image_0000002589324737.png?HW-CC-KV=V1&HW-CC-Date=20260429T053040Z&HW-CC-Expire=86400&HW-CC-Sign=84AEE5B1AD491CA0C9E3D11E05B4DFD49EF4E38DC34286E1F19405DEC369AD27)
2. 再次打开相同的网站，点击用户名或者密码框中时，会弹出密码保险箱的下拉框。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/1Cl5deJcSqiP52VJKlK_6w/zh-cn_image_0000002589244675.png?HW-CC-KV=V1&HW-CC-Date=20260429T053040Z&HW-CC-Expire=86400&HW-CC-Sign=252032075A82233E32FB514B81808995D476BD29B3E488E3499E894341FD9EBB)
3. 选择下拉框中的用户名，通过认证，就能直接在网页中填入之前保存的用户名、密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/aXcyjnpxQ9mDSAr903N2Dg/zh-cn_image_0000002558764870.png?HW-CC-KV=V1&HW-CC-Date=20260429T053040Z&HW-CC-Expire=86400&HW-CC-Sign=CE8041D7890A41EFA3D6B656EA32B8712372E7644D715F290F34D1A402F057F5)
4. 也可以点击下拉框中的“使用其他账号”，选择密码保险箱中保存的其他账号。认证后在网页中填入选择的用户名、密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/hN9t0pBbS9WHX-atiuKclw/zh-cn_image_0000002558605214.png?HW-CC-KV=V1&HW-CC-Date=20260429T053040Z&HW-CC-Expire=86400&HW-CC-Sign=E853604374CD7D12823A6394613E10CAEA9D8AB0BCEB45B917641C88664391E7)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/yszWyKRcSt6Wcn_Y5SLNjA/zh-cn_image_0000002589324739.png?HW-CC-KV=V1&HW-CC-Date=20260429T053040Z&HW-CC-Expire=86400&HW-CC-Sign=64FE0923346E92D481D270682BCE59F86306466B1B64561369C4F6A942B8EE6F)

【案例2】：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/9gTV9wnMR2SpNqGH7yoEaA/zh-cn_image_0000002589244677.png?HW-CC-KV=V1&HW-CC-Date=20260429T053040Z&HW-CC-Expire=86400&HW-CC-Sign=E3537249892AAACDA78BF65B9FE95C1FC038FE47A216B1AFCADAF1700B5B4B44)

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
