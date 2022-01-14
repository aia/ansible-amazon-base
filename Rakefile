require 'mixlib/shellout'

def shellout(cmd)
  Mixlib::ShellOut.new(cmd, :live_stream => STDOUT, :timeout => 3600).run_command
end

namespace :ruby do
  desc 'Show installed gems'
  task :gems_list do
    shellout('bundler list')
  end

  desc 'Update dependencies'
  task :gems_update do
    puts 'Running Bundler Update'
    shellout('bundler update')
  end
end

namespace :python do
  desc 'Update poetry dependencies'
  task :poetry_update do
    puts 'Running Poetry Update'
    shellout('poetry update')
    puts '========================='
    puts 'Updating requirements.txt'
    shellout('poetry export -f requirements.txt -o requirements.txt --without-hashes')
  end
end

namespace :vagrant do
  desc 'Show Vagrant boxes'
  task :boxes do
    shellout('vagrant box list')
  end
end

namespace :docker do
  desc 'Show Docker contexts'
  task :context do
    shellout('docker context list')
  end
end
