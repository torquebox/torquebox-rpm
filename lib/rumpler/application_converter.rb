
module Rumpler

  class ApplicationConverter

    attr_accessor :app_dir
    attr_accessor :output_dir

    def initialize(app_dir, output_dir)
      @app_dir = app_dir
      @output_dir = output_dir
    end

    def dump()
      dump_dependencies()
      dump_root_spec()
    end

    def dump_dependencies()
      puts "Dumping for #{app_dir}"

      gemfile = File.join( app_dir, 'Gemfile' )

      ENV['BUNDLE_GEMFILE'] = gemfile
      puts "Parsing #{gemfile} to #{output_dir}"
      @gemfile_converter = GemfileConverter.new( gemfile, output_dir )
      @gemfile_converter.resolve!
      @gemfile_converter.dump()
    end

   def dump_root_spec()
   end

  end

end
