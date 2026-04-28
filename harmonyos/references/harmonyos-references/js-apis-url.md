---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-url
title: @ohos.url (URL字符串解析)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.url (URL字符串解析)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b30e6a19bc8ab0e6154143daaa4c957ddcffcf27457e7e9d6225add7dcb8f2ae
---

URL代表的是统一资源定位符，本模块提供了常用的工具函数，实现了解析URL字符串和构造[URL](js-apis-url.md#url)对象等功能。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { url } from '@kit.ArkTS';
```

## URLParams9+

PhonePC/2in1TabletTVWearable

URLParams是一个用于解析、构造和操作URL参数的实用类。该类提供了统一的接口来处理参数维度（如查询参数、路径参数等）。

### constructor9+

PhonePC/2in1TabletTVWearable

constructor(init?: string[][] | Record<string, string> | string | URLParams)

URLParams的构造函数。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| init | string[][] | Record<string, string> | string | URLParams | 否 | 入参对象。  - string[][]：字符串二维数组。  - Record<string, string>：对象列表。  - string：字符串。  - URLParams：对象。  - 默认值：null。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**示例：**

```
1. // 通过string[][]方式构造URLParams对象：
2. let objectParams = new url.URLParams([ ['user1', 'abc1'], ['query2', 'first2'], ['query3', 'second3'] ]);
3. // 通过Record<string, string>方式构造URLParams对象：
4. let objectParams1 = new url.URLParams({"fod" : '1' , "bard" : '2'});
5. // 通过string方式构造URLParams对象：
6. let objectParams2 = new url.URLParams('?fod=1&bard=2');
7. // 通过url对象的search属性构造URLParams对象：
8. let urlObject = url.URL.parseURL('https://developer.mozilla.org/?fod=1&bard=2');
9. let objectParams3 = new url.URLParams(urlObject.search);
10. // 通过url对象的params属性获取URLParams对象：
11. let urlObject1 = url.URL.parseURL('https://developer.mozilla.org/?fod=1&bard=2');
12. let objectParams4 = urlObject1.params;
```

### append9+

PhonePC/2in1TabletTVWearable

append(name: string, value: string): void

将新的键值对插入到查询字符串。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 需要插入搜索参数的键名。 |
| value | string | 是 | 需要插入搜索参数的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
2. let paramsObject = new url.URLParams(urlObject.search.slice(1));
3. paramsObject.append('fod', '3');
```

### delete9+

PhonePC/2in1TabletTVWearable

delete(name: string): void

删除指定名称的键值对。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 需要删除的键值名称。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
2. let paramsObject = new url.URLParams(urlObject.search.slice(1));
3. paramsObject.delete('fod');
```

### getAll9+

PhonePC/2in1TabletTVWearable

getAll(name: string): string[]

获取指定名称的所有键对应值的集合。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 指定的键值名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 返回指定名称的所有键对应值的集合。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
2. let params = new url.URLParams(urlObject.search.slice(1));
3. params.append('fod', '3'); // Add a second value for the fod parameter.
4. console.info(params.getAll('fod').toString()) // Output ["1","3"].
```

### entries9+

PhonePC/2in1TabletTVWearable

entries(): IterableIterator<[string, string]>

返回一个ES6的迭代器，迭代器的每一项都是一个Array。Array的第一项是name，Array的第二项是value。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<[string, string]> | 返回一个ES6的迭代器。 |

**示例：**

```
1. let paramsObject = new url.URLParams("keyName1=valueName1&keyName2=valueName2");
2. let pair = paramsObject.entries();
3. for (let item of pair) {
4. console.info(item[0] + '=' + item[1]);
5. }
6. // keyName1=valueName1
7. // keyName2=valueName2
```

### forEach9+

PhonePC/2in1TabletTVWearable

forEach(callbackFn: (value: string, key: string, searchParams: URLParams) => void, thisArg?: Object): void

通过回调函数来遍历URLParams实例对象上的键值对。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackFn | function | 是 | 回调函数。 |
| thisArg | Object | 否 | callbackFn被调用时用作this值，默认值是本对象。 |

**表1** callbackFn的参数说明

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 当前遍历到的键值。 |
| key | string | 是 | 当前遍历到的键名。 |
| searchParams | [URLParams](js-apis-url.md#urlparams9) | 是 | 当前调用forEach方法的实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. const myURLObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
2. myURLObject.params.forEach((value, name, searchParams) => {
3. console.info(name, value, myURLObject.params === searchParams);
4. });
```

### get9+

PhonePC/2in1TabletTVWearable

get(name: string): string | null

获取指定名称对应的第一个值。

说明

若查找一个不存在的键值对名称时返回值为undefined。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 指定键值对的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | null | 返回第一个值，如果没找到，返回 null。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let paramsObject = new url.URLParams('name=Jonathan&age=18');
2. let name = paramsObject.get("name"); // is the string "Jonathan"
3. let age = paramsObject.get("age"); // is the string "18"
4. let getObj = paramsObject.get("abc"); // undefined
```

### has9+

PhonePC/2in1TabletTVWearable

has(name: string): boolean

判断一个指定的键名对应的值是否存在。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 要查找的参数的键名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否存在相对应的key值，存在返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
2. let paramsObject = new url.URLParams(urlObject.search.slice(1));
3. let result = paramsObject.has('bard');
```

### set9+

PhonePC/2in1TabletTVWearable

set(name: string, value: string): void

将与name关联的URLSearchParams对象中的值设置为value。

如果存在名称为name的键值对，请将第一个键值对的值设置为value并删除所有其他值。如果不是，则将键值对附加到查询字符串。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 将要设置的参数的键值名。 |
| value | string | 是 | 所要设置的参数值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
2. let paramsObject = new url.URLParams(urlObject.search.slice(1));
3. paramsObject.set('baz', '3'); // Add a third parameter.
```

### sort9+

PhonePC/2in1TabletTVWearable

sort(): void

对包含在此对象中的所有键值对进行排序。排序顺序是根据键的Unicode代码点。该方法使用稳定的排序算法（保留具有相等键的键值对之间的相对顺序）。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. let paramsObject = new url.URLParams("c=3&a=9&b=4&d=2"); // Create a test URLParams object
2. paramsObject.sort(); // Sort the key/value pairs
3. console.info(paramsObject.toString()); // Display the sorted query string // Output a=9&b=4&c=3&d=2
```

### keys9+

PhonePC/2in1TabletTVWearable

keys(): IterableIterator<string>

返回一个包含所有键值对的name的ES6迭代器。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<string> | 返回一个包含所有键值对的name的ES6迭代器。 |

**示例：**

```
1. let paramsObject = new url.URLParams("key1=value1&key2=value2");
2. let keys = paramsObject.keys();
3. for (let key of keys) {
4. console.info(key);
5. }
6. // key1
7. // key2
```

### values9+

PhonePC/2in1TabletTVWearable

values(): IterableIterator<string>

返回一个包含所有键值对的value的ES6迭代器。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<string> | 返回一个包含所有键值对的value的ES6迭代器。 |

**示例：**

```
1. let paramsObject = new url.URLParams("key1=value1&key2=value2");
2. let values = paramsObject.values();
3. for (let value of values) {
4. console.info(value);
5. }
6. // value1
7. // value2
```

### [Symbol.iterator]9+

PhonePC/2in1TabletTVWearable

[Symbol.iterator](): IterableIterator<[string, string]>

返回一个ES6的迭代器，迭代器的每一项都是一个Array。Array的第一项是name，Array的第二项是value。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<[string, string]> | 返回一个ES6的迭代器。 |

**示例：**

```
1. const paramsObject = new url.URLParams('fod=bay&edg=bap');
2. let iter = paramsObject[Symbol.iterator]();
3. for (let pair of iter) {
4. console.info(pair[0] + ', ' + pair[1]);
5. }
6. // fod, bay
7. // edg, bap
```

### toString9+

PhonePC/2in1TabletTVWearable

toString(): string

返回序列化为字符串的搜索参数，必要时对字符进行百分比编码。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回序列化为字符串的搜索参数，必要时对字符进行百分比编码。 |

**示例：**

```
1. let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
2. let params = new url.URLParams(urlObject.search.slice(1));
3. params.append('fod', '3');
4. console.info(params.toString()); // Output 'fod=1&bard=2&fod=3'
```

## URL

PhonePC/2in1TabletTVWearable

用于解析、构造、规范、编码对应的URL字符串。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| hash | string | 否 | 否 | 获取和设置URL的片段部分。**元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| host | string | 否 | 否 | 获取和设置URL的主机部分。**元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| hostname | string | 否 | 否 | 获取和设置URL的主机名部分，不带端口。**元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| href | string | 否 | 否 | 获取和设置序列化的URL。**元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| origin | string | 是 | 否 | 获取URL源的只读序列化。**元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| password | string | 否 | 否 | 获取和设置URL的密码部分。**元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| pathname | string | 否 | 否 | 获取和设置URL的路径部分。**元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| port | string | 否 | 否 | 获取和设置URL的端口部分。**元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| protocol | string | 否 | 否 | 获取和设置URL的协议部分。**元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| search | string | 否 | 否 | 获取和设置URL的序列化查询部分。**元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| searchParams(deprecated) | [URLSearchParams](js-apis-url.md#urlsearchparamsdeprecated) | 是 | 否 | 获取URLSearchParams表示URL查询参数的对象。  - **说明：** 此属性从API version 7开始支持，从API version 9开始被废弃。建议使用params9+替代。 |
| params9+ | [URLParams](js-apis-url.md#urlparams9) | 是 | 否 | 获取URLParams表示URL查询参数的对象。**元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| username | string | 否 | 否 | 获取和设置URL的用户名部分。**元服务API**：从API version 11开始，该接口支持在元服务中使用。 |

说明

在解析URL字符串时，如果入参中的port内容是当前protocol的默认端口，那么port将被解析为空字符串。默认端口为：

| 协议 | 默认端口 |
| --- | --- |
| http: | 80 |
| https: | 443 |
| ftp: | 21 |
| gopher: | 70 |
| ws: | 80 |
| wss: | 443 |

**示例：**

```
1. let that = url.URL.parseURL('http://username:password@host:8080/directory/file?foo=1&bar=2#fragment');
2. console.info("hash " + that.hash); // hash #fragment
3. console.info("host " + that.host); // host host:8080
4. console.info("hostname " + that.hostname); // hostname host
5. console.info("href " + that.href); // href http://username:password@host:8080/directory/file?foo=1&bar=2#fragment
6. console.info("origin " + that.origin); // origin http://host:8080
7. console.info("password " + that.password); // password password
8. console.info("pathname " + that.pathname); // pathname /directory/file
9. console.info("port " + that.port); // port 8080
10. console.info("protocol " + that.protocol); // protocol http:
11. console.info("search " + that.search); // search ?foo=1&bar=2
12. console.info("username " + that.username); // username username
13. // that.params 返回值为URLParams对象
14. console.info("params: foo " + that.params.get("foo")); // params: foo 1

16. let urlObj = url.URL.parseURL('http://testhost:80/directory/file?foo=1');
17. console.info("port " + urlObj.port); // port
18. console.info("toString " + urlObj.toString()); // toString http://testhost/directory/file?foo=1
```

### constructor(deprecated)

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[parseURL9+](js-apis-url.md#parseurl9)替代。

constructor(url: string, base?: string | URL)

URL的构造函数。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 一个表示绝对URL或相对URL的字符串。  如果 url 是相对URL，则需要指定 base，用于解析最终的URL。  如果 url 是绝对URL，则给定的 base 将不会生效。 |
| base | string | URL | 否 | 入参字符串或者对象，默认值是undefined。  - string：字符串。  - URL：URL对象。 |

**示例：**

```
1. let mm = 'https://username:password@host:8080';
2. let a = new url.URL("/", mm); // Output 'https://username:password@host:8080/';
3. let b = new url.URL(mm); // Output 'https://username:password@host:8080/';
4. new url.URL('path/path1', b); // Output 'https://username:password@host:8080/path/path1';
5. let c = new url.URL('/path/path1', b);  // Output 'https://username:password@host:8080/path/path1';
6. new url.URL('/path/path1', c); // Output 'https://username:password@host:8080/path/path1';
7. new url.URL('/path/path1', a); // Output 'https://username:password@host:8080/path/path1';
8. new url.URL('/path/path1', "https://www.exampleUrl/fr-FR/toot"); // Output https://www.exampleUrl/path/path1
9. new url.URL('/path/path1', ''); // Raises a TypeError exception as '' is not a valid URL
10. new url.URL('/path/path1'); // Raises a TypeError exception as '/path/path1' is not a valid URL
11. new url.URL('https://www.example.com', ); // Output https://www.example.com/
12. new url.URL('https://www.example.com', b); // Output https://www.example.com/
```

### constructor9+

PhonePC/2in1TabletTVWearable

constructor()

URL的无参构造函数。parseURL调用后返回一个URL对象，不单独使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

### parseURL9+

PhonePC/2in1TabletTVWearable

static parseURL(url: string, base?: string | URL): URL

解析URL。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 一个表示绝对URL或相对URL的字符串。  如果 url 是相对URL，则需要指定 base，用于解析最终的URL。  如果 url 是绝对URL，则给定的 base 将不会生效。 |
| base | string | URL | 否 | 入参字符串或者对象，默认值是undefined。  - string：字符串。当第一个参数是相对URL时，该参数需符合URL标准。  - URL：URL对象。  - 在url是相对URL时使用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [URL](js-apis-url.md#url) | 返回创建的URL对象。 |

说明

当入参url是相对URL时，调用该接口解析后的URL并不是简单地将入参url和base直接拼接。url内容为相对路径格式时，会相对于base的当前目录进行解析，包括base中path字段最后一个斜杠前的所有路径片段，但不包括其后的部分（参照示例中url1）。url内容为指向根目录的格式时，会相对于 base 的原始地址（origin）进行解析（参照示例中url2）。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200002 | Invalid url string. |

**示例：**

```
1. let mm = 'https://username:password@host:8080/test/test1/test3';
2. let urlObject = url.URL.parseURL(mm);
3. let result = urlObject.toString(); // Output 'https://username:password@host:8080/test/test1/test3'
4. // url内容为相对路径格式时，此时base参数的path为test/test1,解析后的URL的path为/test/path2/path3
5. let url1 = url.URL.parseURL('path2/path3', 'https://www.example.com/test/test1'); // Output 'https://www.example.com/test/path2/path3'
6. // url内容为指向根目录的格式时，此时base参数的path为/test/test1/test3，解析后的URL的path为/path1/path2
7. let url2 = url.URL.parseURL('/path1/path2', urlObject); // Output 'https://username:password@host:8080/path1/path2'
8. url.URL.parseURL('/path/path1', "https://www.exampleUrl/fr-FR/toot"); // Output 'https://www.exampleUrl/path/path1'
9. url.URL.parseURL('/path/path1', ''); // Raises a TypeError exception as '' is not a valid URL
10. url.URL.parseURL('/path/path1'); // Raises a TypeError exception as '/path/path1' is not a valid URL
11. url.URL.parseURL('https://www.example.com', ); // Output 'https://www.example.com/'
12. url.URL.parseURL('https://www.example.com', urlObject); // Output 'https://www.example.com/'
```

### toString

PhonePC/2in1TabletTVWearable

toString(): string

将解析过后的URL转化为字符串。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转化后的字符串。 |

**示例：**

```
1. const urlObject = url.URL.parseURL('https://username:password@host:8080/directory/file?query=pppppp#qwer=da');
2. let result = urlObject.toString(); // Output 'https://username:password@host:8080/directory/file?query=pppppp#qwer=da'
```

### toJSON

PhonePC/2in1TabletTVWearable

toJSON(): string

将解析过后的URL转化为JSON字符串。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转化后的JSON字符串。 |

**示例：**

```
1. const urlObject = url.URL.parseURL('https://username:password@host:8080/directory/file?query=pppppp#qwer=da');
2. let result = urlObject.toJSON();
```

## URLSearchParams(deprecated)

PhonePC/2in1TabletTVWearable

URLSearchParams接口定义了一些处理URL查询字符串的实用方法，从API version 9开始废弃，建议使用[URLParams](js-apis-url.md#urlparams9)。

### constructor(deprecated)

PhonePC/2in1TabletTVWearable

constructor(init?: string[][] | Record<string, string> | string | URLSearchParams)

URLSearchParams的构造函数。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[URLParams.constructor9+](js-apis-url.md#constructor9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| init | string[][] | Record<string, string> | string | URLSearchParams | 否 | 入参对象。  - string[][]：字符串二维数组。  - Record<string, string>：对象列表。  - string：字符串。  - URLSearchParams：对象。  - 默认值：undefined。 |

**示例：**

```
1. let objectParams = new url.URLSearchParams([ ['user1', 'abc1'], ['query2', 'first2'], ['query3', 'second3'] ]);
2. let objectParams1 = new url.URLSearchParams({"fod" : '1' , "bard" : '2'});
3. let objectParams2 = new url.URLSearchParams('?fod=1&bard=2');
4. let urlObject = new url.URL('https://developer.mozilla.org/?fod=1&bard=2');
5. let params = new url.URLSearchParams(urlObject.search);
```

### append(deprecated)

PhonePC/2in1TabletTVWearable

append(name: string, value: string): void

将新的键值对插入到查询字符串。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[URLParams.append9+](js-apis-url.md#append9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 需要插入搜索参数的键名。 |
| value | string | 是 | 需要插入搜索参数的值。 |

**示例：**

```
1. let urlObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
2. let paramsObject = new url.URLSearchParams(urlObject.search.slice(1));
3. paramsObject.append('fod', '3');
```

### delete(deprecated)

PhonePC/2in1TabletTVWearable

delete(name: string): void

删除指定名称的键值对。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[URLParams.delete9+](js-apis-url.md#delete9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 需要删除的键值名称。 |

**示例：**

```
1. let urlObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
2. let paramsObject = new url.URLSearchParams(urlObject.search.slice(1));
3. paramsObject.delete('fod');
```

### getAll(deprecated)

PhonePC/2in1TabletTVWearable

getAll(name: string): string[]

获取指定名称的所有键值对。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[URLParams.getAll9+](js-apis-url.md#getall9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 指定的键值名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 返回指定名称的所有键值对。 |

**示例：**

```
1. let urlObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
2. let params = new url.URLSearchParams(urlObject.search.slice(1));
3. params.append('fod', '3'); // Add a second value for the fod parameter.
4. console.info(params.getAll('fod').toString()) // Output ["1","3"].
```

### entries(deprecated)

PhonePC/2in1TabletTVWearable

entries(): IterableIterator<[string, string]>

返回一个ES6的迭代器，迭代器的每一项都是一个Array。Array的第一项是name，Array的第二项是value。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[URLParams.entries9+](js-apis-url.md#entries9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<[string, string]> | 返回一个ES6的迭代器。 |

**示例：**

```
1. let searchParamsObject = new url.URLSearchParams("keyName1=valueName1&keyName2=valueName2");
2. let iter = searchParamsObject.entries();
3. for (let pair of iter) {
4. console.info(pair[0]+ ', '+ pair[1]);
5. }
6. // keyName1, valueName1
7. // keyName2, valueName2
```

### forEach(deprecated)

PhonePC/2in1TabletTVWearable

forEach(callbackFn: (value: string, key: string, searchParams: URLSearchParams) => void, thisArg?: Object): void

通过回调函数来遍历URLSearchParams实例对象上的键值对。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[URLParams.forEach9+](js-apis-url.md#foreach9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackFn | function | 是 | 回调函数。 |
| thisArg | Object | 否 | callbackFn被调用时用作this值，默认值是本对象。 |

**表1** callbackFn的参数说明

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 当前遍历到的键值。 |
| key | string | 是 | 当前遍历到的键名。 |
| searchParams | [URLSearchParams](js-apis-url.md#urlsearchparamsdeprecated) | 是 | 当前调用forEach方法的实例对象。 |

**示例：**

```
1. const myURLObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
2. myURLObject.searchParams.forEach((value, name, searchParams) => {
3. console.info(name, value, myURLObject.searchParams === searchParams);
4. });
```

### get(deprecated)

PhonePC/2in1TabletTVWearable

get(name: string): string | null

获取指定名称对应的第一个值。

说明

若查找一个不存在的键值对名称时返回值为undefined，从API version 7开始支持，从API version 9开始废弃，建议使用[URLParams.get9+](js-apis-url.md#get9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 指定键值对的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | null | 返回第一个值，如果没找到，返回 null。 |

**示例：**

```
1. let paramsObject = new url.URLSearchParams('name=Jonathan&age=18');
2. let name = paramsObject.get("name"); // is the string "Jonathan"
3. let age = paramsObject.get("age"); // is the string '18'
4. let getObj = paramsObject.get("abc"); // undefined
```

### has(deprecated)

PhonePC/2in1TabletTVWearable

has(name: string): boolean

判断一个指定的键名对应的值是否存在。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[URLParams.has9+](js-apis-url.md#has9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 要查找的参数的键名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否存在相对应的key值。存在返回true，否则返回false。 |

**示例：**

```
1. let urlObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
2. let paramsObject = new url.URLSearchParams(urlObject.search.slice(1));
3. paramsObject.has('bard') === true;
```

### set(deprecated)

PhonePC/2in1TabletTVWearable

set(name: string, value: string): void

将与name关联的URLSearchParams对象中的值设置为value。如果存在名称为name的键值对，请将第一个键值对的值设置为value并删除所有其他值。如果不是，则将键值对附加到查询字符串。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[URLParams.set9+](js-apis-url.md#set9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 将要设置的参数的键值名。 |
| value | string | 是 | 所要设置的参数值。 |

**示例：**

```
1. let urlObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
2. let paramsObject = new url.URLSearchParams(urlObject.search.slice(1));
3. paramsObject.set('baz', '3'); // Add a third parameter.
```

### sort(deprecated)

PhonePC/2in1TabletTVWearable

sort(): void

对包含在此对象中的所有键值对进行排序，并返回undefined。排序顺序是根据键的Unicode代码点。该方法使用稳定的排序算法 （即，将保留具有相等键的键值对之间的相对顺序）。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[URLParams.sort9+](js-apis-url.md#sort9)替代。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. let searchParamsObject = new url.URLSearchParams("c=3&a=9&b=4&d=2"); // Create a test URLSearchParams object
2. searchParamsObject.sort(); // Sort the key/value pairs
3. console.info(searchParamsObject.toString()); // Display the sorted query string // Output a=9&b=4&c=3&d=2
```

### keys(deprecated)

PhonePC/2in1TabletTVWearable

keys(): IterableIterator<string>

返回一个所有键值对的name的ES6迭代器。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[URLParams.keys9+](js-apis-url.md#keys9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<string> | 返回一个所有键值对的name的ES6迭代器。 |

**示例：**

```
1. let searchParamsObject = new url.URLSearchParams("key1=value1&key2=value2");
2. let keys = searchParamsObject.keys();
3. for (let key of keys) {
4. console.info(key);
5. }
6. // key1
7. // key2
```

### values(deprecated)

PhonePC/2in1TabletTVWearable

values(): IterableIterator<string>

返回一个所有键值对的value的ES6迭代器。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[URLParams.values9+](js-apis-url.md#values9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<string> | 返回一个所有键值对的value的ES6迭代器。 |

**示例：**

```
1. let searchParams = new url.URLSearchParams("key1=value1&key2=value2");
2. let values = searchParams.values();
3. for (let value of values) {
4. console.info(value);
5. }
6. // value1
7. // value2
```

### [Symbol.iterator](deprecated)

PhonePC/2in1TabletTVWearable

[Symbol.iterator](): IterableIterator<[string, string]>

返回一个ES6的迭代器，迭代器的每一项都是一个Array。Array的第一项是name，Array的第二项是value。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[URLParams.[Symbol.iterator]9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-url#symboliterator9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<[string, string]> | 返回一个ES6的迭代器。 |

**示例：**

```
1. const paramsObject = new url.URLSearchParams('fod=bay&edg=bap');
2. let pairs = paramsObject[Symbol.iterator]();
3. for (let pair of pairs) {
4. console.info(pair[0] + ', ' + pair[1]);
5. }
6. // fod, bay
7. // edg, bap
```

### toString(deprecated)

PhonePC/2in1TabletTVWearable

toString(): string

返回序列化为字符串的搜索参数，必要时对字符进行百分比编码。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[URLParams.toString9+](js-apis-url.md#tostring9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回序列化为字符串的搜索参数，必要时对字符进行百分比编码。 |

**示例：**

```
1. let urlObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
2. let params = new url.URLSearchParams(urlObject.search.slice(1));
3. params.append('fod', '3');
4. console.info(params.toString()); // Output 'fod=1&bard=2&fod=3'
```
