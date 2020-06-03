CRReq (Card Range Request)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<ThreeDSecure>
  <Message id="999">
	<CRReq>
	  <version>1.0.1</version>
	  <pan>4444333322221111</pan>
	  <Merchant>
    <acqBIN>411111</acqBIN>
    <merID>99000001</merID>
    <!--<password>99000001</password>-->
	  </Merchant>
	  <Browser>
		<deviceCategory>0</deviceCategory>
		<accept>*/*</accept>
		<userAgent>curl/7.27.0</userAgent>
	  </Browser>
	</CRReq>
  </Message>
</ThreeDSecure>
```
CRRes

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ThreeDSecure>
  <Message id="999">
    <CRRes>
      <version>1.0.1</version>
      <CR>
        <begin>4005559876540</begin>
        <end>4005559876541</end>
        <action>A</action>
      </CR>
      <CR>
        <begin>4000000000000000</begin>
        <end>4931039828002001</end>
        <action>A</action>
      </CR>
      <CR>
        <begin>4012010000000000009</begin>
        <end>4012010000000000010</end>
        <action>A</action>
      </CR>
      <serialNumber>1</serialNumber>
    </CRRes>
  </Message>
</ThreeDSecure>
```