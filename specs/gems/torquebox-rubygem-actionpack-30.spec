%global tree_prefix  torquebox-
%global ruby_sitelib /opt/jruby/lib/ruby/site_ruby/1.8
%global gem_dir      /opt/jruby/lib/ruby/gems/1.8
%global bin_dir      /opt/jruby/bin
%global gem_name     actionpack
%global gem_instdir  %{gem_dir}/gems/%{gem_name}-%{version}
%global ruby_abi     1.8-java

Name: torquebox-rubygem-actionpack-30
Version: 3.0.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
BuildArch: noarch
Summary: Web-flow and rendering framework putting the VC in MVC (part of Rails)
URL: http://www.rubyonrails.org
Source0: http://rubygems.org/gems/actionpack-3.0.0.gem

Provides: %{tree_prefix}rubygem(%{gem_name}) = %{version}

Requires: ruby(abi) = %{ruby_abi}

Requires: %{tree_prefix}rubygem(activesupport) = 3.0.0
Requires: %{tree_prefix}rubygem(activemodel) = 3.0.0
Requires: %{tree_prefix}rubygem(builder) => 2.1.2
Requires: %{tree_prefix}rubygem(builder) < 2.2
Requires: %{tree_prefix}rubygem(i18n) => 0.4.1
Requires: %{tree_prefix}rubygem(i18n) < 0.5
Requires: %{tree_prefix}rubygem(rack) => 1.2.1
Requires: %{tree_prefix}rubygem(rack) < 1.3
Requires: %{tree_prefix}rubygem(rack-test) => 0.5.4
Requires: %{tree_prefix}rubygem(rack-test) < 0.6
Requires: %{tree_prefix}rubygem(rack-mount) => 0.6.12
Requires: %{tree_prefix}rubygem(rack-mount) < 0.7
Requires: %{tree_prefix}rubygem(tzinfo) => 0.3.23
Requires: %{tree_prefix}rubygem(tzinfo) < 0.4
Requires: %{tree_prefix}rubygem(erubis) => 2.6.6
Requires: %{tree_prefix}rubygem(erubis) < 2.7

%description

Web apps on Rails. Simple, battle-tested conventions for building and testing MVC web applications. Works with any Rack-compatible server.

%prep

%build

%install

rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{bin_dir}
install -m 755 -d %{buildroot}%{gem_dir}
install -m 755 -d %{buildroot}%{gem_dir}/gems/actionpack-3.0.0/lib
gem install --local --bindir %{buildroot}%{bin_dir} --install-dir %{buildroot}%{gem_dir} --force --ignore-dependencies --platform ruby %{SOURCE0}

%clean

rm -rf %{buildroot}

%files

%defattr(-, root, root, -)
%{bin_dir}/
%{gem_dir}/gems/actionpack-3.0.0/
%{gem_dir}/cache/actionpack-3.0.0.gem
%{gem_dir}/specifications/actionpack-3.0.0.gemspec
%doc %{gem_dir}/doc/actionpack-3.0.0

%changelog

