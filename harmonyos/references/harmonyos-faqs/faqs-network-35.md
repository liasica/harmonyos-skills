---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-35
title: 三方件@ohos/axios中发起post请求，如何以queryParams形式传递参数
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 三方件@ohos/axios中发起post请求，如何以queryParams形式传递参数
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a688a03f649e2b24b661ba701c8a29621517405349ad14303cf396daf9256e15
---

* 方式一：使用axios.post接口时，Url.URLParams需要转换为字符串并拼接到URL后面。

  ```typescript
  let params: url.URLParams = new url.URLParams()
  params.append('fod' ,'1')
  params.append('bard','2')
  axios.post('https://developer.mozilla.org/?' + params.toString()).then((res: AxiosResponse) => {
    let message = "request result: " + JSON.stringify(res.data);
  }).catch((err:AxiosError) => {
    let message = "request error: " + err.message;
  })
  ```
* 方式二：使用axios接口，请求参数写在config对象的params中。

  ```typescript
  axios({ url: 'https://developer.mozilla.org/?', method: 'post', params: { fod: '1', bard: '2', } }).then((res: AxiosResponse) => {
    let message = "request result: " + JSON.stringify(res.data);
  }).catch((err:AxiosError) => {
    let message = "request error: " + err.message;
  })
  ```

**参考链接**

[URLParams](../harmonyos-references/js-apis-url.md#urlparams9)
