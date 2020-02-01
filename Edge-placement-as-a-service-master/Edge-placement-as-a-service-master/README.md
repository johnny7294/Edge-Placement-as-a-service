# Edge-placement-as-a-service
a cloud service is provided to multiple tenants, such that each tenant can create multiple virtual private cloud and in turn deploy their network inside it. Along with this a DNS and Nginx solution are given, where tenant can access its network and make some desired altercation and also user can request for tenant’s content and acquire it. in our case “user” can access the content placed on the edge device. Let’s see how does the user access the tenant’s content; Firstly, when user arrives at the entry point at hypervisor 2 it requests for specific content of the Tenant. A DNS query goes to the DNS forwarder which in turn looks into its DNS records and finds a tenants DNS server for which the request is intended to. Then tenant’s DNS server on receiving the request looks it’s records and gives response which includes nearest Edge’s IP address. Once the request for the content is reached at the Edge, it will resolve by giving the content to the user. Keeping the track of all the content in the Edge and extracting a particular content for each request is done by Nginx web server.  