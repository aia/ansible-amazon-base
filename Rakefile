
namespace :ruby do
  desc 'Show installed gems'
  task :gems_list do
    puts %x[bundler list]
  end

  desc 'Update dependencies'
  task :gems_update do
    puts 'Running Bundler Update'
    puts %x[bundler update]
  end
end

namespace :python do
  desc 'Update poetry dependencies'
  task :poetry_update do
    puts 'Running Poetry Update'
    puts %x[poetry update]
    puts '========================='
    puts 'Updating requirements.txt'
    puts %x[poetry export -f requirements.txt -o requirements.txt --without-hashes]
  end
end

namespace :vagrant do
  desc 'Show Vagrant boxes'
  task :boxes do
    puts %x[vagrant box list]
  end
end

namespace :docker do
  desc 'Show Docker contexts'
  task :context do
    puts %x[docker context list]
  end
end
