%define torquebox_version 1.0.0.Beta22
%define jruby_version     1.5.3


%global ruby_sitelib /opt/jruby/lib/ruby/site_ruby/1.8
%global gem_dir      /opt/jruby/lib/ruby/gems/1.8
%global bin_dir      /opt/jruby/bin
%global lib_dir      /opt/jruby/lib
%global ruby_abi     1.8-java

%global gem_cache_dir   ./jruby/lib/ruby/gems/1.8/cache

%global gem_install  gem install --local --bindir %{buildroot}%{bin_dir} --install-dir %{buildroot}%{gem_dir} --force --ignore-dependencies 

%global _binaries_in_noarch_packages_terminate_build 0

Summary:        TorqueBox Rubygems
Name:           torquebox-rubygems
Version:        %{torquebox_version}
Release:        1
License:        LGPL
BuildArch:      noarch
Group:          Applications/System
Source0:        http://repository.torquebox.org/maven2/releases/org/torquebox/torquebox-dist/1.0.0.Beta22/torquebox-dist-%{torquebox_version}-bin.zip

Requires: ruby(abi)       = %{ruby_abi}
Requires: torquebox-jruby = %{jruby_version}

Provides: torquebox-rubygem(org.torquebox.rake-support)               = %{torquebox_version}
Provides: torquebox-rubygem(org.torquebox.torquebox-container)        = %{torquebox_version}
Provides: torquebox-rubygem(org.torquebox.torquebox-messaging)        = %{torquebox_version}
Provides: torquebox-rubygem(org.torquebox.torquebox-messaging)        = %{torquebox_version}
Provides: torquebox-rubygem(org.torquebox.torquebox-naming-client)    = %{torquebox_version}
Provides: torquebox-rubygem(org.torquebox.torquebox-naming-container) = %{torquebox_version}
Provides: torquebox-rubygem(org.torquebox.vfs-1.0.0.Beta22)           = %{torquebox_version}

%description
  The TorqueBox Rubygems 

%prep
%setup -n torquebox-%{torquebox_version}

%install

rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{bin_dir}
install -m 755 -d %{buildroot}%{lib_dir}

install -m 755 -d %{buildroot}%{gem_dir}

%{gem_install} --platform ruby %{gem_cache_dir}/org.torquebox.rake-support-%{torquebox_version}.gem
%{gem_install} --platform java %{gem_cache_dir}/org.torquebox.torquebox-container-foundation-%{torquebox_version}-java.gem
%{gem_install} --platform java %{gem_cache_dir}/org.torquebox.torquebox-messaging-client-%{torquebox_version}-java.gem
%{gem_install} --platform java %{gem_cache_dir}/org.torquebox.torquebox-messaging-container-%{torquebox_version}-java.gem
%{gem_install} --platform java %{gem_cache_dir}/org.torquebox.torquebox-naming-client-%{torquebox_version}-java.gem
%{gem_install} --platform java %{gem_cache_dir}/org.torquebox.torquebox-naming-container-%{torquebox_version}-java.gem
%{gem_install} --platform ruby %{gem_cache_dir}/org.torquebox.vfs-%{torquebox_version}.gem

cp ./jruby/lib/jboss-*.jar %{buildroot}%{lib_dir}


%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
/

%changelog
* Mon Oct 04 2010 Bob McWhirter 
- Initial release
