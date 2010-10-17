%global tree_prefix  torquebox-
%global ruby_sitelib /opt/jruby/lib/ruby/site_ruby/1.8
%global gem_dir      /opt/jruby/lib/ruby/gems/1.8
%global bin_dir      /opt/jruby/bin
%global gem_name     simple-navigation
%global gem_instdir  %{gem_dir}/gems/%{gem_name}-%{version}
%global ruby_abi     1.8-java

Name: torquebox-rubygem-simple-navigation-20
Version: 2.6.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
BuildArch: noarch
Summary: Simple Navigation is a ruby library for creating navigations (with multiple levels) for your Ruby on Rails application
URL: http://github.com/andi/simple-navigation
Source0: http://rubygems.org/gems/simple-navigation-2.6.0.gem

Provides: %{tree_prefix}rubygem(%{gem_name}) = %{version}

Requires: ruby(abi) = %{ruby_abi}


%description

With the simple-navigation gem installed you can easily create multilevel navigations for your Ruby on Rails applications. The navigation is defined in a single configuration file. It supports automatic as well as explicit highlighting of the currently active navigation.

%prep

%build

%install

rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{bin_dir}
install -m 755 -d %{buildroot}%{gem_dir}
install -m 755 -d %{buildroot}%{gem_dir}/gems/simple-navigation-2.6.0/lib
gem install --local --bindir %{buildroot}%{bin_dir} --install-dir %{buildroot}%{gem_dir} --force --ignore-dependencies --platform ruby %{SOURCE0}

%clean

rm -rf %{buildroot}

%files

%defattr(-, root, root, -)
%{bin_dir}/
%{gem_dir}/gems/simple-navigation-2.6.0/
%{gem_dir}/cache/simple-navigation-2.6.0.gem
%{gem_dir}/specifications/simple-navigation-2.6.0.gemspec
%doc %{gem_dir}/doc/simple-navigation-2.6.0

%changelog

