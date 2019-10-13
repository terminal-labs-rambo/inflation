APPNAME=inflation
PYTHONVERSION = 3.6.9

help:
	@echo "usage: make [command]"

download_python_environment_manager:
	@if test ! -d "maintenance";then \
		sudo rm -rf maintenance; \
		sudo su -m $(SUDO_USER) -c "mkdir -p .tmp"; \
		sudo su -m $(SUDO_USER) -c "cd .tmp; wget https://github.com/terminal-labs/python-environment-manager/archive/master.zip"; \
		sudo su -m $(SUDO_USER) -c "cd .tmp; unzip -qq master.zip"; \
		sudo su -m $(SUDO_USER) -c "cp -r .tmp/python-environment-manager-master/maintenance/. maintenance"; \
		sudo rm -rf .tmp/python-environment-manager-master; \
		sudo rm .tmp/master.zip; \
	fi

vagrant-pyenv: download_python_environment_manager
	@sudo bash maintenance/general/pyenv/build.sh $(APPNAME) $(SUDO_USER) vagrant

vagrant-conda: download_python_environment_manager
	@sudo bash maintenance/general/conda/build.sh $(APPNAME) $(SUDO_USER) vagrant

mac-pyenv: download_python_environment_manager
	@sudo bash maintenance/general/pyenv/build.sh $(APPNAME) $(SUDO_USER) mac
	@sudo bash maintenance/general/pyenv/emit_activation_script.sh $(APPNAME) $(SUDO_USER) mac

mac-conda: download_python_environment_manager
	@sudo bash maintenance/general/conda/build.sh $(APPNAME) $(SUDO_USER) mac
	@sudo bash maintenance/general/conda/emit_activation_script.sh $(APPNAME) $(SUDO_USER) mac

linux-pyenv: download_python_environment_manager
	@sudo bash maintenance/general/pyenv/build.sh $(APPNAME) $(SUDO_USER) linux
	@sudo bash maintenance/general/pyenv/emit_activation_script.sh $(APPNAME) $(SUDO_USER) linux

linux-conda: download_python_environment_manager
	@sudo bash maintenance/general/conda/build.sh $(APPNAME) $(SUDO_USER) linux
	@sudo bash maintenance/general/conda/emit_activation_script.sh $(APPNAME) $(SUDO_USER) linux
