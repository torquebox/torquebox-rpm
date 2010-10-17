%global tree_prefix  torquebox-
%global ruby_sitelib /opt/jruby/lib/ruby/site_ruby/1.8
%global gem_dir      /opt/jruby/lib/ruby/gems/1.8
%global bin_dir      /opt/jruby/bin
%global gem_name     builder
%global gem_instdir  %{gem_dir}/gems/%{gem_name}-%{version}
%global ruby_abi     1.8-java

Name: torquebox-rubygem-builder-22
Version: 2.1.2
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
BuildArch: noarch
Summary: Builders for MarkUp
URL: http://onestepback.org
Source0: http://rubygems.org/gems/builder-2.1.2.gem

Provides: %{tree_prefix}rubygem(%{gem_name}) = %{version}

Requires: ruby(abi) = %{ruby_abi}


%description

Builder provides a number of builder objects that make creating structured data simple to do.  Currently the following builder objects are supported:  * XML Markup * XML Events

%prep

%build

%install

rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{bin_dir}
install -m 755 -d %{buildroot}%{gem_dir}
install -m 755 -d %{buildroot}%{gem_dir}/gems/builder-2.1.2/lib
gem install --local --bindir %{buildroot}%{bin_dir} --install-dir %{buildroot}%{gem_dir} --force --ignore-dependencies --platform ruby %{SOURCE0}

%clean

rm -rf %{buildroot}

%files

%defattr(-, root, root, -)
%{bin_dir}/
%{gem_dir}/gems/builder-2.1.2/
%{gem_dir}/cache/builder-2.1.2.gem
%{gem_dir}/specifications/builder-2.1.2.gemspec
%doc %{gem_dir}/doc/builder-2.1.2
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/README
%doc %{gem_instdir}/doc/releases/builder-1.2.4.rdoc
%doc %{gem_instdir}/doc/releases/builder-2.0.0.rdoc
%doc %{gem_instdir}/doc/releases/builder-2.1.1.rdoc

%changelog

