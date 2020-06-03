VeReq (Verify Enrollment Request)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<ThreeDSecure>
  <Message id="999">
	<VEReq>
	  <version>1.0.2</version>
	  <pan>4444333322221111</pan>
	  <Merchant>
		<acqBIN>411111</acqBIN>
		<merID>99000001</merID>
		<password>99000001</password>
	  </Merchant>
	  <Browser>
		<deviceCategory>0</deviceCategory>
		<accept>*/*</accept>
		<userAgent>curl/7.27.0</userAgent>
	  </Browser>
	</VEReq>
  </Message>
</ThreeDSecure>
```

VeRes
```xml
<?xml version="1.0" encoding="UTF-8"?>
<ThreeDSecure>
  <Message id="999">
    <VERes>
      <version>1.0.2</version>
      <CH>
        <enrolled>Y</enrolled>
        <acctID>A0fTY+pKUTu/6hcZWZJiAA==</acctID>
      </CH>
      <url>https://dropit.3dsecure.net:9443/PIT/ACS</url>
      <protocol>ThreeDSecure</protocol>
    </VERes>
  </Message>
</ThreeDSecure>
```