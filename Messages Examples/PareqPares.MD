PaReq (Payment request)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ThreeDSecure>
	<Message id="123-123-123-123-123-123">
		<PAReq>
			<version>1.0.2</version>
			<Merchant>
				<acqBIN>510069</acqBIN>
				<merID>123123123123123</merID>
				<name>MerchantName</name>
				<country>643</country>
				<url>http://asdas.as</url>
			</Merchant>
			<Purchase>
				<xid>U3Vic2NyaWJlX0B3ZWJyMGNr</xid>
				<date>20181004 21:34:21</date>
				<amount>202000</amount>
				<purchAmount>202000</purchAmount>
				<currency>643</currency>
				<exponent>2</exponent>
				<desc>AcquirerName</desc>
			</Purchase>
			<CH>
				<acctID>DYasdVQAOX6as3dfcxccwzPCR6Q74eS5</acctID>
				<expiry>2209</expiry>
			</CH>
		</PAReq>
	</Message>
</ThreeDSecure>
```

PaRes

```xml
<ThreeDSecure>
	<Message id="epg365ea016-1066-45ad-937d-f31a44152ec0">
		<PARes id="msg.9561553.signed">
			<version>1.0.2</version>
			<Merchant>
				<acqBIN>123456</acqBIN>
				<merID>11111111</merID>
			</Merchant>
			<Purchase>
				<xid>YTBjMGRjZDdiYmIxNGI2ZjgyMTk=</xid>
				<date>20181010 20:51:55</date>
				<purchAmount>10100</purchAmount>
				<currency>643</currency>
				<exponent>2</exponent>
			</Purchase>
			<pan>0000000000001111</pan>
			<TX>
				<time>20181010 20:52:27</time>
				<status>Y</status>
				<cavv>hixYBNtnUMwTYwAACr/QCGcAAAA=</cavv>
				<eci>01</eci>
				<cavvAlgorithm>3</cavvAlgorithm>
			</TX>
		</PARes>
		<Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
			<SignedInfo xmlns="http://www.w3.org/2000/09/xmldsig#">
				<CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>
				<SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
				<Reference URI="#msg.9561553.signed">
					<DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
					<DigestValue>ScK5xxZbAg4oemxS9/NgtjgAfBk=</DigestValue>
				</Reference>
			</SignedInfo>
			<SignatureValue>
ohgrkauaoAccj6HRHUU2eTqizGSCJXiv5/w9Kbz/UQvD2u1q
--- signature ----
c3lKloGCzq9T2gGJnYIkTfwwFiRrr5rmhWHIMwuto/CtI0Kz
9C/onA==
</SignatureValue>
			<KeyInfo>
				<X509Data>
					<X509Certificate>MIIEbjCCA1agAwIBAgIRAPJdoUCN3GjNvgHmV9hKzK0wDQYJKoZIhvcNAQEFBQAwgYYxCzAJBgNVBAYTAlVTMR0wGwYDVQQKExRNYXN0ZXJDYXJ
					--- certificate ---
						gUm9vdCBDQYIQQ3EBfDozHhKp3pmzcHr6ZzANBgkqhkiG9w0BAQUFAAOCAQEAH7O2fgleorhtS/IjCKZLGr5haXinLaSW87A7kLJcj/2g10YvzIOjcBGdfQhoxAyEuyXksCNjjfyRojcg==</X509Certificate>
					<X509Certificate>MIIEbjCCA1agAwIBAgIRAPJdoUCN3GjNvgHmV9hKzK0wDQYJKoZIhvcNAQEFBQAwgYYxCzAJBgNVBAYTAlVTMR0wGwYDVQQKExRNYXN0ZXJDYXJ
					--- certificate ---
						gUm9vdCBDQYIQQ3EBfDozHhKp3pmzcHr6ZzANBgkqhkiG9w0BAQUFAAOCAQEAH7O2fgleorhtS/IjCKZLGr5haXinLaSW87A7kLJcj/2g10YvzIOjcBGdfQhoxAyEuyXksCNjjfyRojcg==</X509Certificate>
					<X509Certificate>MIIEbjCCA1agAwIBAgIRAPJdoUCN3GjNvgHmV9hKzK0wDQYJKoZIhvcNAQEFBQAwgYYxCzAJBgNVBAYTAlVTMR0wGwYDVQQKExRNYXN0ZXJDYXJ
					--- certificate ---
						gUm9vdCBDQYIQQ3EBfDozHhKp3pmzcHr6ZzANBgkqhkiG9w0BAQUFAAOCAQEAH7O2fgleorhtS/IjCKZLGr5haXinLaSW87A7kLJcj/2g10YvzIOjcBGdfQhoxAyEuyXksCNjjfyRojcg==</X509Certificate>
				</X509Data>
			</KeyInfo>
		</Signature>
	</Message>
</ThreeDSecure>
```