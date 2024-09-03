# Instructions

To deploy the project effectively to the remote instance and automate everything in the pipeline.

## STEP - 1 
Create a EC2 instance or Lightsail instance, Run the `instance_startup.sh` script in the server. Get the IP of host system.

## STEP - 2
Create a key-pair for ssh authentication to this instance `NOTE: create key pair without password`

## STEP - 3
Create a PAT token for your docker registry

## STEP - 4
Cosign key pair is already available in the repository folder. Create a new pair with password if you need it.
Default key password: `i66icgx68+o3-j:`

## Final Step
Add everything to secrets and varibables in repository as shown below,

SSH_PRIVATE_KEY
DEPLOYMENT_USER
DEPLOYMENT_HOST
DOCKER_USERNAME
DOCKER_PAT
COSIGN_PASSWORD
COSIGN_KEY

*NOTE: Additionally You can customize the image name in `build` Action file and SBOM artifact name in the `SBOM` Action file*
