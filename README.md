# Ansible Amazon Base Repository
<!-- markdownlint-disable-file MD014 -->

- [Ansible Amazon Base Repository](#ansible-amazon-base-repository)
  - [About](#about)
  - [Setting Up Ansible Environment](#setting-up-ansible-environment)
    - [Configuring Python VENV and Ansible](#configuring-python-venv-and-ansible)
    - [Editor Configuration](#editor-configuration)
  - [Setting Up VirtualBox Environment](#setting-up-virtualbox-environment)
    - [Install VirtualBox and Vagrant](#install-virtualbox-and-vagrant)
    - [Configuring Test Kitchen](#configuring-test-kitchen)
    - [Downloading Amazon Linux v2 Vagrant Box](#downloading-amazon-linux-v2-vagrant-box)
    - [Build an Optimized Amazon Linux 2 Vagrant Box](#build-an-optimized-amazon-linux-2-vagrant-box)
    - [Environment Variable Overwrites for Kitchen](#environment-variable-overwrites-for-kitchen)
  - [Running Test Kitchen](#running-test-kitchen)
  - [Running Integration Tests](#running-integration-tests)
  - [Running Ansible Playbooks on AWS Instances](#running-ansible-playbooks-on-aws-instances)
  - [Example Project: Build a Local Docker/Containerd Server VM](#example-project-build-a-local-dockercontainerd-server-vm)
  - [Ansible References](#ansible-references)

## About

Ansible Amazon Base Repository is an MVP monorepo to rapidly develop scalable, reliable,
high-quality components for Amazon Linux instance configuration management.

## Setting Up Ansible Environment

### Configuring Python VENV and Ansible

Note: This document assumes that you are working on Mac

1. Create a new virtual environment with pyenv

   ```text
   $ pyenv virtualenv miniconda3-latest ansible
   ```

2. Activate your new python virtual environment

   ```text
   $ pyenv activate ansible
   ```

3. Install poetry

   ```text
   $ conda install poetry
   ```

4. Install dependencies

   ```text
   $ poetry install
   ```

5. Check ansible

   ```text
   $ ansible --version
   ```

### Editor Configuration

Code editors are major software development productivity tools. VSCode is a game changer.

VSCode should be configured for typical Python development with the following extensions:

- [Ansible](https://marketplace.visualstudio.com/items?itemName=redhat.ansible)
- [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
- [Trailing Spaces](https://marketplace.visualstudio.com/items?itemName=shardulm94.trailing-spaces)
- [Blank line at the End of File](https://marketplace.visualstudio.com/items?itemName=riccardoNovaglia.missinglineendoffile)
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [Markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Test Explorer](https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer)
- [Python Test Explorer](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter)
- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
- [Remote SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
- [Remote Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [VirtualBox](https://marketplace.visualstudio.com/items?itemName=acherkashin.virtualbox-extension)
- [Vagrant](https://marketplace.visualstudio.com/items?itemName=bbenoist.vagrant)
- [Ruby](https://marketplace.visualstudio.com/items?itemName=rebornix.Ruby)
- [Ruby Solargraph](https://marketplace.visualstudio.com/items?itemName=castwide.solargraph)
- [Github](https://marketplace.visualstudio.com/items?itemName=KnisterPeter.vscode-github)
- [Github Actions](https://marketplace.visualstudio.com/items?itemName=cschleiden.vscode-github-actions)
- [Gitlens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)

VSCode should be configured to associate most of the files in the repository with Ansible.
Check that your ansible files have Ansible set in the "Select Language Mode".
In VSCode the difference between YAML and Ansible Language Mode is night and day.
Example .vscode/settings.json

```json
{
  "files.associations": {
    "kitchen*": "yaml",
    "*.yml": "ansible"
  },
}
```

Python should be setup with the following:

```json
    "editor.renderWhitespace": "all",
    "editor.rulers": [
        80,
        100,
        120
    ],
    "[python]": {
        "editor.tabSize": 4,
        "editor.insertSpaces": true,
        "editor.formatOnSave": true
    },
    "[yaml]": {
        "editor.insertSpaces": true,
        "editor.tabSize": 2,
        "editor.autoIndent": "none",
        "editor.quickSuggestions": {
            "other": true,
            "comments": false,
            "strings": true
        },
        "editor.formatOnPaste": true
    },
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.banditEnabled": true,
    "python.linting.banditArgs": [
        "-x",
        "./tests",
        "-r",
    ],
    "python.linting.pylintArgs": [
        "--disable=C0301,C0111,E0402,W0702,W0108,W0703"
    ],
    "python.linting.pycodestyleEnabled": true,
    "python.linting.pycodestyleArgs": [
        "--ignore E501"
    ],
    "python.formatting.provider": "black",
    "python.languageServer": "Pylance",
    "python.envFile": "/Users/current.user/.vspyenv",
    "python.testing.pytestArgs": [
        "-s",
        "-vvvv"
    ],
    "pythonTestExplorer.testFramework": "pytest",
    "markdownlint.config": {
        "MD013": {
            "line_length": 120,
            "tables": false,
            "code_blocks": false
        },
        "MD025": false,
        "MD033": false,
        "MD036": false,
        "MD041": false
    },
    "testExplorer.hideEmptyLog": false,
```

## Setting Up VirtualBox Environment

Access to local VMs running Amazon Linux helps rapidly and safely iterate on Ansible code.

### Install VirtualBox and Vagrant

[VirtualBox](https://www.virtualbox.org/) can be installed with Homebrew. However, every once in a while the latest build
of VirtualBox has a broken functionality. At the time of writing, VirtualBox 6.1.28 has a broken Host Network Manager.
Good build of VirtualBox is [6.1.26](https://download.virtualbox.org/virtualbox/6.1.26/VirtualBox-6.1.26-145957-OSX.dmg).
Install Virtual Box from the link.

[Vagrant](https://github.com/hashicorp/vagrant) is a HashiCorp Ruby project to provide VirtualBox abstraction.
Use Homebrew to install vagrant

```text
$ brew install vagrant
```

### Configuring Test Kitchen

[Test Kitchen](https://github.com/test-kitchen/test-kitchen) is a Ruby project to automate
Infrastructure as Code development life-cyle.

Install RVM

```text
$ gpg --keyserver hkp://pool.sks-keyservers.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB

$ \curl -sSL https://get.rvm.io | bash -s stable --ruby
```

Add RVM to your profile

```bash
# Add RVM
[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm"
```

Change directory to anything other than ansible-amazon-base and change back to have RVM pull a ruby version
and create a gemset.

```text
$ cd ..
$ cd ansible-amazon-base/
ruby-3.0.0 - #gemset created /home/current.user/.rvm/gems/ruby-3.0.0@ansible-kitchen
ruby-3.0.0 - #generating ansible-kitchen wrappers.............
```

After RVM configures Gemset, run bundler to install gems

```text
$ bundle install
```

### Downloading Amazon Linux v2 Vagrant Box

Amazon Linux v2 is a feature-rich Linux distribution maintained by Amazon. Amazon page about [Amazon Linux Images](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-linux-2-virtual-machine.html#amazon-linux-2-virtual-machine-download)
lists various formats available, including [Amazon Linux v2 virtualbox](https://cdn.amazonlinux.com/os-images/2.0.20211005.0/virtualbox/).

Older Amazon Linux v2 vagrant box can be downloaded from [HashiCorp Vagrant Cloud](https://app.vagrantup.com/bento/boxes/amazonlinux-2).

Import vagrant box:

```text
$ vagrant box add amazon2 <downloaded box>
$ vagrant box list
```

Latest Amazon Linux v2 box can be built from [Chef Bento](https://github.com/chef/bento/blob/main/packer_templates/amazonlinux/README_FIRST.md)
project. Disabling Amazon SSM is a consideration.

### Build an Optimized Amazon Linux 2 Vagrant Box

Default Amazon Linux 2 vagrant box does not come with Ansible installed.
Any time we run kitchen with the default Amazon Linux 2 box, kitchen will spend time installing Ansible.
In order to save development time, we will build a box that includes Ansible and Docker.

Run kitchen converge with kitchen.box.yml

```text
$ KITCHEN_YAML=kitchen.box.yml kitchen converge box
```

List running VirtualBox VMs and make note of the full name of the kitchen-ansible-amazon-base-box-amazon VM

```text
$ VBoxManage list vms
"kitchen-ansible-amazon-base-box-amazon-cb9dedd7-fd27-4344-b026-bd3a2b7a340e" {9cf5ed90-d3a0-4e95-b742-6c9249c0cf34}
```

Run vagrant to export kitchen-ansible-amazon-base-box-amazon

```text
$ vagrant package --base kitchen-ansible-amazon-base-box-amazon-cb9dedd7-fd27-4344-b026-bd3a2b7a340e
==> kitchen-ansible-amazon-base-box-amazon-cb9dedd7-fd27-4344-b026-bd3a2b7a340e: Attempting graceful shutdown of VM...
==> kitchen-ansible-amazon-base-box-amazon-cb9dedd7-fd27-4344-b026-bd3a2b7a340e: Clearing any previously set forwarded ports...
==> kitchen-ansible-amazon-base-box-amazon-cb9dedd7-fd27-4344-b026-bd3a2b7a340e: Exporting VM...
==> kitchen-ansible-amazon-base-box-amazon-cb9dedd7-fd27-4344-b026-bd3a2b7a340e: Compressing package to: /Users/current.user/work/ansible-amazon-base/package.box
```

Import package.box as amazon2-ansible

```text
$ vagrant box add amazon2-ansible package.box
$ vagrant box list
amazon2         (virtualbox, 0)
amazon2-ansible (virtualbox, 0)
```

Remove kitchen instance

```text
KITCHEN_YAML=kitchen.box.yml kitchen destroy box
```

Remove package.box from the local folder

### Environment Variable Overwrites for Kitchen

Kitchen will use amazon2-ansible box by default.
If you are using a different box, you can set KITCHEN_ANSIBLE_BOX environment variable.

## Running Test Kitchen

Change directory to playbooks and run

```text
$ kitchen list
```

To create a VirtualBox VM and apply an Ansible playbook run

```text
$ kitchen converge docker
```

To destroy a created VM run

```text
$ kitchen destroy docker
```

To connect to a VM run

```text
$ kitchen ssh docker
```

## Running Integration Tests

Integration tests are written in [TestInfra](https://github.com/pytest-dev/pytest-testinfra).
To run tests

```text
$ kitchen verify docker
```

## Running Ansible Playbooks on AWS Instances

In order to run Ansible Playbooks on AWS instances, first configure
ANSIBLE_ROLES_PATH to point to the roles directory of the repository, e.g.

```text
$ export ANSIBLE_ROLES_PATH=/Users/current.user/work/ansible-amazon-base/roles
```

Also configure ~/.ansible.cfg to format Ansible output as a more readable YAML

```ini
[defaults]
stdout_callback = yaml
```

Choose a playbook and run Ansible

```text
$ ansible-playbook -v -u ec2-user --private-key ~/.ssh/<instance>.pem -i <instance_ip>, playbooks/gst/gst_jupyter.yml
```

## Example Project: Build a Local Docker/Containerd Server VM

Why bother with Docker Desktop when you can build your own Containerd Server?

Check "Host Network Manager" in the File menu of your VirtualBox. Add an interface and make note of the subnet.

Edit kitchen.yml containerd suit and set private_network to a static IP of your choice.

```yaml
  - name: containerd
    provisioner:
      name: ansible_playbook
      playbook: ./playbooks/docker/docker.yml
    driver:
      vm_hostname: containerd.local
      network:
        - ['private_network', {ip: '192.168.56.121'}]
```

Run kitchen converge

```text
$ kitchen converge containerd
...
       PLAY RECAP *********************************************************************
       localhost                  : ok=5    changed=1    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0

       Downloading files from <containerd-amazon>
       Finished converging <containerd-amazon> (0m5.54s).
-----> Test Kitchen is finished. (1m15.18s)
```

SSH into your Containerd VM.
Change vagrant's user password from 'vagrant' to something secure.
Add your SSH key to ~/.ssh/authorized_keys. Change permissions on /var/run/docker.sock.

```text
$ ssh vagrant@192.168.56.121
vagrant@192.168.56.121's password:
Last login: Mon Nov 15 05:47:31 2021 from 10.0.2.2

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/

This system is built by the Bento project by Chef Software
More information can be found at https://github.com/chef/bento

[vagrant@containerd ~]$ passwd
Changing password for user vagrant.
Changing password for vagrant.
(current) UNIX password:
New password:
Retype new password:
passwd: all authentication tokens updated successfully.
[vagrant@containerd ~]$ vi ~/.ssh/authorized_keys
[vagrant@containerd ~]$ sudo chmod a+rw /var/run/docker.sock
exit
logout
Connection to 192.168.56.121 closed.
```

Create a new Docker context:

```text
$ docker context create containerd1 --docker "host=ssh://vagrant@192.168.56.121"
containerd
Successfully created context "containerd1"
$ docker context use containerd1
$ docker context ls
NAME            DESCRIPTION                               DOCKER ENDPOINT                KUBERNETES ENDPOINT   ORCHESTRATOR
containerd1 *                                             ssh://vagrant@192.168.56.121
default         Current DOCKER_HOST based configuration   unix:///var/run/docker.sock                          swarm
```

Start using your new Containerd server:

```text
$ docker version
Client: Docker Engine - Community
 Version:           20.10.10
 API version:       1.41
 Go version:        go1.17.2
 Git commit:        b485636f4b
 Built:             Fri Oct 15 14:45:13 2021
 OS/Arch:           darwin/amd64
 Context:           containerd1
 Experimental:      true

Server:
 Engine:
  Version:          20.10.7
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.15.14
  Git commit:       b0f5bc3
  Built:            Tue Sep 28 19:56:28 2021
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.4.6
  GitCommit:        d71fcd7d8303cbf684402823e425e9dd2e99285d
 runc:
  Version:          1.0.0
  GitCommit:        84113eef6fc27af1b01b3181f31bbaf708715301
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```

## Ansible References

- [Ansible 101 - Episode 1 - Introduction to Ansible](https://www.youtube.com/watch?v=goclfp6a2IQ)
- [Ansible 101 - Episode 2 - Ad-hoc Tasks and Inventory](https://www.youtube.com/watch?v=7kVfqmGtDL8)
- [Ansible 101 - Episode 3 - Introduction to Playbooks](https://www.youtube.com/watch?v=WNmKjtWtqIc)
- [Ansible 101 - Episode 4 - Your First Real-World Playbook](https://www.youtube.com/watch?v=SLW4LX7lbvE)
- [Ansible 101 - Episode 5 - Playbook Handlers, Environment Vars, and Variables](https://www.youtube.com/watch?v=HU-dkXBCPdU)
- [Ansible 101 - Episode 6 - Ansible Vault and Roles](https://www.youtube.com/watch?v=JFweg2dUvqM)
- [Make Your Ansible Playbooks Flexible, Maintainable, and Scalable](https://www.youtube.com/watch?v=kNDL13MJG6Y)
