
require 'bundler'
require 'fileutils'

module Rumpler
  class GemfileConverter
  
    DEP_EXCLUDES = [
      %r(^org.torquebox),
      %r(^rails$),
      %r(^rack$),
    ]

    SPEC_EXCLUDES = {
      'columnize'=>'03',
      'rake'=>'08',
      'rspec'=>'13',
      'ruby-debug'=>'010',
      'ruby-debug-base'=>'010',
      'sources'=>'00',
      'rack'=>'*',
    }

    attr_accessor :gemfile
    attr_accessor :ruby_config
    attr_accessor :definition

    attr_accessor :output_dir
  
    def initialize(gemfile, output_dir, ruby_config=Config.new)
      @gemfile = gemfile
      @ruby_config = ruby_config
      @output_dir = output_dir
    end
  
    def resolve!()
      current_platform = Gem.platforms.compact.last
      @definition = Bundler::Definition.build( @gemfile, @gemfile + '.lock', true )
      @definition.dependencies.reject! do |dep| 
        result = false
        DEP_EXCLUDES.each do |regexp|
          if ( regexp =~ dep.name )
            puts "excluding #{dep.name}"
            result = true 
          end
        end
        result
      end
      @definition.resolve_remotely!
    end
  
    def dump()
      dump_specs()
    end

    def dump_specs()
      @definition.specs.each do |spec|
        exclude_version = SPEC_EXCLUDES[ spec.name ]
        if ( ! exclude_version.nil? )
          puts spec.version.inspect
          puts spec.version.segments.inspect
          test = "#{spec.version.segments[0]}#{spec.version.segments[1]}"
          puts "compare #{test} to #{exclude_version.inspect}"
          if ( ( exclude_version.to_s == '*' ) || [ exclude_version ].flatten.include?( test ) )
            puts "Skipping #{spec.name} #{spec.version}"
            next
          end
        end
        dump_spec(spec )
      end
    end
  
    def dump_spec(gemspec)
      converter = GemspecConverter.new( ruby_config, gemspec )
      rpmspec_path = File.join( output_dir, converter.rpm_name + '.spec' )
      puts "Writing #{rpmspec_path}"
      FileUtils.mkdir_p( File.dirname( rpmspec_path ) )
      File.open( rpmspec_path, 'w' ) do |file|
        converter.out = file
        converter.dump
      end
    end
  
  end
end
