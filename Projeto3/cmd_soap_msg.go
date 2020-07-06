package auxi

import (
	"bytes"
	"crypto/sha256"
	"crypto/tls"
	"log"
	"encoding/base64"
	"net/http"
	"strings"
)

func get_wsdl(env int) string{
	wsdl := [2]string{"https://preprod.cmd.autenticacao.gov.pt/Ama.Authentication.Frontend/CCMovelDigitalSignature.svc?wsdl", "https://cmd.autenticacao.gov.pt/Ama.Authentication.Frontend/CCMovelDigitalSignature.svc?wsdl"}
	return wsdl[env]
}


func parseCert(res string) []string{
	split := strings.Split(res, "</?GetCertificateResult>")
	allcerts := split[1]
	tempcerts := strings.Split(allcerts, "-----BEGIN CERTIFICATE-----")
	total := len(tempcerts)
	for i:= 0; i < total; i++ {
		tempcerts[i] = "-----BEGIN CERTIFICATE-----\n" + tempcerts[i]
	}
	var certificates []string
	certificates[0] = strings.Replace(certificates[0], "&#xD;", "", -1)
	certificates[1] = strings.Replace(certificates[1], "&#xD;", "", -1)
	certificates[2] = strings.Replace(certificates[2], "&#xD;", "", -1)
	return certificates
}

func getcertificate(url string, applicationId string, userId string) []string{
	encoded64 := base64.StdEncoding.EncodeToString([]byte(applicationId))

	xmlstring := strings.TrimSpace(`
     <Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
       <Body>
         <GetCertificate xmlns="http://Ama.Authentication.Service/">
             <applicationId>[base64Binary?]</applicationId>
             <userId>[string?]</userId>
         </GetCertificate>
       </Body>
     </Envelope>`,
	)

	xmlstring = strings.Replace(xmlstring, "[base64Binary?]", encoded64, 1)
	xmlstring = strings.Replace(xmlstring, "[string?]", userId, 1)

	payload := []byte(xmlstring)

	soapAction := "urn:GetCertificate"
	httpMethod := "POST"

	req, err := http.NewRequest(httpMethod, url, bytes.NewReader(payload))
	if err != nil {
		log.Fatal("Error on creating request object. ", err.Error())
	}

	req.Header.Set("Content-type", "text/xml")
	req.Header.Set("SOAPAction", soapAction)

	client := &http.Client{
		Transport: &http.Transport{
			TLSClientConfig: &tls.Config{
				InsecureSkipVerify: true,
			},
		},
	}

	res, err := client.Do(req)
	if err != nil {
		log.Fatal("Error on dispatching request. ", err.Error())
	}

	
	buf := new(bytes.Buffer)
	buf.ReadFrom(res.Body)
	newStr := buf.String()

	return parseCert(newStr)
}


func hash(message string) string{
	hasher := sha256.New()
	hasher.Write([]byte(message))
	str := base64.StdEncoding.EncodeToString(hasher.Sum(nil))
	return str
}

func parseCCmovelsign(res string) string {
	splited := strings.Split(res, "</?a:ProcessId>")
	return splited[1]
}

func ccmovelsign(url string, applicationId string, docName string, userId string, userPin string, hasher string) string{
	encoded64 := base64.StdEncoding.EncodeToString([]byte(applicationId))

	xmlstring := strings.TrimSpace(`
  <Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
    <Body>
        <CCMovelSign xmlns="http://Ama.Authentication.Service/">
            <!-- Optional -->
            <request>
                <ApplicationId xmlns="http://schemas.datacontract.org/2004/07/Ama.Structures.CCMovelSignature">[applicationId]</ApplicationId>
                <DocName xmlns="http://schemas.datacontract.org/2004/07/Ama.Structures.CCMovelSignature">[docName]</DocName>
                <Hash xmlns="http://schemas.datacontract.org/2004/07/Ama.Structures.CCMovelSignature">[base64Binary]</Hash>
                <Pin xmlns="http://schemas.datacontract.org/2004/07/Ama.Structures.CCMovelSignature">[userPin]</Pin>
                <UserId xmlns="http://schemas.datacontract.org/2004/07/Ama.Structures.CCMovelSignature">[userId]</UserId>
            </request>
        </CCMovelSign>
    </Body>
  </Envelope>`,
	)

	xmlstring = strings.Replace(xmlstring, "[applicationId]", encoded64, 1)
	xmlstring = strings.Replace(xmlstring, "[docName]", docName, 1)
	xmlstring = strings.Replace(xmlstring, "[Hash]", hasher, 1)
	xmlstring = strings.Replace(xmlstring, "[userPin]", userPin, 1)
	xmlstring = strings.Replace(xmlstring, "[userId]", userId, 1)


	payload := []byte(xmlstring)

	soapAction := "urn:CCMovelSign"
	httpMethod := "POST"

	req, err := http.NewRequest(httpMethod, url, bytes.NewReader(payload));
	if err != nil {
		log.Fatal("Error on creating request object. ", err.Error())}

	req.Header.Set("Content-type", "text/xml")
	req.Header.Set("SOAPAction", soapAction)

	client := &http.Client{
		Transport: &http.Transport{
			TLSClientConfig: &tls.Config{
				InsecureSkipVerify: true,
			},
		},
	}

	res, err := client.Do(req)
	if err != nil {
		log.Fatal("Error on dispatching request. ", err.Error())
	}
	
	
	buf := new(bytes.Buffer)
	buf.ReadFrom(res.Body)
	newStr := buf.String()

	processId := parseCCmovelsign(newStr)
	return processId

}

func parseOptRes(res string) string{
	parsed := strings.Split(res, "</?a:Signature>")
	signature := parsed[1]
	return signature
}

func validateotp(url string, otp string, processId string, applicationId string) string{
	encoded64 := base64.StdEncoding.EncodeToString([]byte(applicationId))

	xmlstring := strings.TrimSpace(`
  <Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
    <Body>
        <ValidateOtp xmlns="http://Ama.Authentication.Service/">
            <code>[otp]</code>
            <processId>[processId]</processId>
            <applicationId>[applicationId]</applicationId>
        </ValidateOtp>
    </Body>
  </Envelope>`,
	)

	xmlstring = strings.Replace(xmlstring, "[otp]", otp, 1)
	xmlstring = strings.Replace(xmlstring, "[processId]", processId, 1)
	xmlstring = strings.Replace(xmlstring, "[applicationId]", encoded64, 1)

	payload := []byte(xmlstring)

	soapAction := "urn:GetCertificate"
	httpMethod := "POST"

	req, err := http.NewRequest(httpMethod, url, bytes.NewReader(payload))
	if err != nil {
		log.Fatal("Error on creating request object. ", err.Error())
	}

	req.Header.Set("Content-type", "text/xml")
	req.Header.Set("SOAPAction", soapAction)

	client := &http.Client{
		Transport: &http.Transport{
			TLSClientConfig: &tls.Config{
				InsecureSkipVerify: true,
			},
		},
	}

	res, err := client.Do(req)
	if err != nil {
		log.Fatal("Error on dispatching request. ", err.Error())
	}
	
	
	buf := new(bytes.Buffer)
	buf.ReadFrom(res.Body)
	newStr := buf.String()

	signature := parseOptRes(newStr)
	return signature
}
