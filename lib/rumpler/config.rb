

module Rumpler
  class Config
    attr_accessor :ruby_sitelib
    attr_accessor :gem_dir
    attr_accessor :bin_dir
    attr_accessor :ruby_abi
  
    attr_accessor :tree_prefix
  
    def initialize()
      @ruby_sitelib = '/opt/jruby/lib/ruby/site_ruby/1.8'
      @gem_dir = '/opt/jruby/lib/ruby/gems/1.8'
      @bin_dir = '/opt/jruby/bin'
      @ruby_abi    = '1.8-java'
      @tree_prefix = 'torquebox-'
    end
  end
end
