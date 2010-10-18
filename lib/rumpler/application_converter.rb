
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
      puts "Dumping #{app_dir}"

      gemfile = File.join( app_dir, 'Gemfile' )

      @gemfile_converter = GemfileConverter.new( gemfile, output_dir )
      @gemfile_converter.dump()
    end

   def dump_root_spec()
   end

  end

end
