---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-114
title: 自定义拦截器写入中文公参在网络请求时变乱码
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 自定义拦截器写入中文公参在网络请求时变乱码
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bd815b3fb529ebc19ddebdad311f1198d81e5e01967ed7557aea7b272e5470c0
---

## 问题现象

自定义拦截器，写入中文公参，写入时正常，网络请求时却变成乱码。代码和抓包记录如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/_GB5okHGRS21MFvh5yr9RQ/zh-cn_image_0000002628770798.png "点击放大")

问题代码示例参考如下：

```screen
private encryptParams(config: InternalAxiosRequestConfig) {
  config.transformRequest = (data: ESObject) => {
    const allParams = new HashMap<string, string>();
    const safeData: ESObject = (data && typeof data === 'object') ? data : {};
    let urlEncode = false
    if (config.headers['Content-Type'] === 'application/x-www-form-urlencoded') {
      urlEncode = true
    }
    allParams.setAll(this.getUserParams(safeData, urlEncode));
    if (allParams.hasKey(this.SIGNATURE_KEY)) {
      allParams.remove(this.SIGNATURE_KEY);
    }
    allParams.set('trader', ClientInfo.getInstance().getTrader());
    allParams.set('traderName', ClientInfo.getInstance().getTraderName());
    allParams.set('provinceId', '1')
    allParams.set('province', '1')
    allParams.set('provinceName', '上海')
    allParams.set('cityName', '上海')
    allParams.set('locateProvinceId','')
    allParams.set('locateCityName','')
    return this.getParamsUrl(allParams, urlEncode)
  }
}
```

## 背景知识

当'content-Type'为'application/x-www-form-urlencoded'时，请求提交的信息主体数据必须在key和value进行URL转码后(encodeURIComponent/encodeURI)，按照键值对"key1=value1&key2=value2&key3=value3"的方式进行编码。

## 问题定位

* application/x-www-form-urlencoded编码格式，是将数据封装成一个字符串，参数名和参数值使用"="拼接，参数之间使用"&"拼接，并且参数会使用encodeURI()进行编码。因此服务器接收到请求时应使用URLDecoder.decode()对key和value进行解码。
* 通过以上代码查看，在headers['Content-Type']使用'application/x-www-form-urlencoded'编码格式时，并未对请求提交的信息主体数据进行转码。

## 分析结论

headers['Content-Type']使用'application/x-www-form-urlencoded'编码格式时，需要对请求提交的信息主体数据进行encodeURIComponent/encodeURI转码。

## 修改建议

建议代码中增加URL转码(encodeURIComponent/encodeURI)例如：

allParams.set('cityName', encodeURIComponent('上海'))
