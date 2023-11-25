## Ideally, you don't want to expose these details at all 

## I haven't been able to achieve this - I am able to encrypt them, but still, 
## private key is being exposed in the code which will reveal this info anyhow.

def gcp_credentials(self):
    credentials = {
        "type": "service_account",
        "project_id": "euphoric-glass-405800",
        "private_key_id": "07941cacdb4eb5ea0e5bd316a70fc7bedf57063f",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCPJt/vYvBl4ZVY\nu5A+uqsj0mnl4oYXJyWbo1NVA8SdUlccbdszJO/8qO/pJ3u1pTRT4SDIPVsY1Jm+\nlhqe+fv9J/1A69qtHIMJJyTMASGM0LQUBJZc4hsoHGwIr7m/X2G7OCi8x8lsZge7\nQiLLz7ZU7uzLbdkKPNDr6ksKcUW5kGFmtzh6kstCNvBFyIe2h3HXTZMiWyh8N49L\nTGwd/9TLXj+zYklMRhc4AStX/BBaMVkwNNuy8ev/3jY2ETFPe4wng7I2+qVhlaKl\n2X6bdC5hMnTy4vK6hiBvKjtxIrEgNByEHYRF+hjKip/Z32hPlfH3U8x6aPfjdaUI\nBKbFOjTzAgMBAAECggEAAVvPGEiKG41ui28MSWwgH7DpjGL//sxCUR3VtqLYhN25\nMe3g/LVHCdDYpg/X3rt4qasjUoMykCPEacim7AdXWum8P5d9ddMlczrJ4J3KIboB\nW4dHng4PT+wlIlf4nVZcaRh5WoFS6hJ11FMmXWTVSC0UVkHuo2g8W2DX4Xt9u+sd\nPyCS/J/LEIJQawg/LkZf02RFcsOgRO72PAepbtjXL5WXVH3dPbU6RC6EQM/jXSeF\nbUCMqsSgKzO29L89u1apTUY2se/4mZpWvb6LaPSuIE8unUnT6H6mkJICXsEXcZW4\nUS009yOvmQnF/1ylwhgzu+Hf5XHkh3yemkPldgOmMQKBgQDDEiL4dqxCa1S0MfYA\nMoWVSydpZoRXahcwxNfR/IdaWRl1Df+txgPKsMtIfjfa4sbgqicn7jAHMyApsuFI\nNu2mVCkl1/pMATteYiywd/VLlppw5RtN86k3+sx8sFGhWqMJrQWNvRmEopKgdeIi\nGq0/WQWGl5Ba32w2VDYW3lRubQKBgQC73UvEDKJXU29vYb+CXK3b0hO1PkcpvaiI\nGQTf458nIhpvPf/wfDAzQOufoOktoQhG0PhVYxfwZRLEtVF2cHg7dbbA/ZhpMQvs\n+eKoerZqND3phPRsq3gMK7FRyHJRWG6Kprk+AZzG5LqofhCRoZTOkh6fEQeLKW3R\n8IPEntOU3wKBgQCPqqzcxzIpHLlemSkvjgX6JUaahulTJAx+W4sD2XOqY9Ku9idn\nSV4Dit+8vVDPwZNtZYO/EdqHguzeKSNoNyQiCvvfJkjubz3VToLRWRfsmreWC/Zn\nG9x2IR03e/gy2PkYqDhd4naHy+Ank4p/SZxs+lhqfvfPJZuiC7VmdEpEpQKBgGft\n5RxwYN8uqVdVHD1iSExzy7NY4MWWxsWEEc5KfqGHnFguVIkWKxQvtip5Ooajr5B9\nyuRyDaxQPjHUnVyIm/tJA/GAWfDX0WEoXNwYBxJ6FEY753y235LcGRzFZ3jZE05h\nLdm/ypu9rgXIuCHY4hnlfEtDgIjcQoUCKeN8elDBAoGBAJm0WKy5Ha8rIXRtJxsE\nYoI0j0vtCh2P2SolvpHqoXZXZADDtUJFcWYF5OVVrZ5mQwUZ99Bw8RTHlHURdz+2\nYAdjtQZmyA5yKpg4mjvLjT41GDYdfgOjMEsmXYfup9LYwp2K176Bg/PMr4bWAEZF\nCAZ7ubZv0O/M48GFUwH4IGkd\n-----END PRIVATE KEY-----\n",
        "client_email": "datacenter-lab@euphoric-glass-405800.iam.gserviceaccount.com",
        "client_id": "116487530686076486188",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/datacenter-lab%40euphoric-glass-405800.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
        }
    return credentials