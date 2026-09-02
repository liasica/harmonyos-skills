---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/attestation-signature-verification-servers
title: 服务器端开发
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 应用真实性证明 > 签名验签识别真实请求 > 服务器端开发
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:32+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:52beb395e98dc6552a61e6625323fed7415a3a2834a26ddadd5461b0769a7228
---

## 使用前提

使用应用公钥对业务请求进行验签的前提是服务器已经完成对密钥证明证书链进行校验和保存应用公钥，相关开发指南请参考：

* [对密钥证明证书链进行校验](device-attestation-servers.md#校验密钥证明证书链)
* [保存应用公钥](device-attestation-servers.md#保存应用公钥)

## 使用应用公钥校验业务请求

应用服务器首先校验挑战值Challenge，然后根据应用公钥ID查找应用公钥。

**说明** 

安全建议：如果应用服务器在保存应用公钥时关联了用户ID，在使用应用公钥对业务请求进行验签时，应该根据应用公钥ID+当前登录的用户ID查找应用公钥。

用服务器再使用应用公钥校验请求中的签名。

**示例：**

```java
import org.bouncycastle.jce.provider.BouncyCastleProvider;

import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.security.InvalidKeyException;
import java.security.KeyFactory;
import java.security.NoSuchAlgorithmException;
import java.security.NoSuchProviderException;
import java.security.PublicKey;
import java.security.Security;
import java.security.Signature;
import java.security.SignatureException;
import java.security.spec.X509EncodedKeySpec;
import java.util.Base64;

public class VerifySignature {
    static {
        Security.addProvider(new BouncyCastleProvider());
    }

    //保存HarmonyOS Hap应用生成的证书公钥的文件名
    static String g_publicKeyFileName = "d:\\attestPublicKey.pem";
    //HarmonyOS Hap应用使用私钥生成的签名数据，base64编码。
    static String g_signedData = "MEUCIQDtlrQa7HQccprCkR0nWTL7N6HEKY9PKN3DTk3aeN0/fQIgeqTrQ+7exiJhwTY3LwT7XhRHV1emOfTYho5qxyektho=";
    //待签名的数据
    static String g_plaintext = "123456";
    //签名算法，与应用端采用的算法保持一致，取值样例：SM3WITHSM2，SHA256withECDSA。
    static String g_signAlg = "SHA256withECDSA";

    public static void main(String[] args) {
        VerifySignature verifySignature = new VerifySignature();
        verifySignature.verifySignature(g_publicKeyFileName, g_plaintext, g_signedData, g_signAlg);
    }

    void verifySignature(String publicKeyFile, String plainText, String signedData, String signAlg) {
        try {
            PublicKey publicKey = readAttestPublicKey(publicKeyFile);
            byte[] signedDataByte = Base64.getDecoder().decode(signedData);
            System.out.println("signedDataByte len=" + signedDataByte.length);
            printBytes(signedDataByte);
            byte[] plainTextBytes = plainText.getBytes();
            System.out.println("plainTextBytes len=" + plainTextBytes.length);
            printBytes(plainTextBytes);
            boolean result = doVerify(publicKey, plainTextBytes, signedDataByte, signAlg);
            System.out.println("Verify signature result: " + result);
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    PublicKey readAttestPublicKey(String publicKeyFileName) throws Exception {
        //todo: 从服务器读取应用公钥
        KeyFactory keyFactory = KeyFactory.getInstance("EC", "BC");
        X509EncodedKeySpec spec = new X509EncodedKeySpec(readFromFile(publicKeyFileName));
        PublicKey publicKey = keyFactory.generatePublic(spec);
        System.out.println("the app public key: \n" + publicKey);
        return publicKey;
    }

    byte[] readFromFile(String fn) throws Exception {
        FileInputStream inputStream = new FileInputStream(fn);
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        byte[] bytes = new byte[1024];
        int len;
        do {
            len = inputStream.read(bytes);
            outputStream.write(bytes, 0, len);
        } while (bytes.length == len);
        inputStream.close();
        return outputStream.toByteArray();
    }

    boolean doVerify(PublicKey publickey, byte[] unsignedData, byte[] signedData, String signAlg) {
        boolean verifyResult = false;
        try {
            Signature signature = Signature.getInstance(signAlg, "BC");
            signature.initVerify(publickey);
            signature.update(unsignedData);
            verifyResult = signature.verify(signedData);
            return verifyResult;
        } catch (NoSuchAlgorithmException | NoSuchProviderException | InvalidKeyException | SignatureException e) {
            e.printStackTrace();
        }
        return verifyResult;
    }

    void printBytes(byte[] byteArray) {
        for (int i = 0; i < byteArray.length; i++) {
            System.out.printf("%02X ", byteArray[i]);
        }
        System.out.println();
    }
}
```
