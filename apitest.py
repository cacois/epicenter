import docker

client = docker.Client(base_url='unix://var/run/docker.sock', version="1.4")

print('Containers: \n\n' + str(client.containers()))
#print('\nLogs: \n\n' + client.logs('jovial_galileo'))
#print('\nImages: \n\n' + str(client.images()))
