%global tree_prefix  torquebox-
%global ruby_sitelib /opt/jruby/lib/ruby/site_ruby/1.8
%global gem_dir      /opt/jruby/lib/ruby/gems/1.8
%global bin_dir      /opt/jruby/bin
%global gem_name     activeresource
%global gem_instdir  %{gem_dir}/gems/%{gem_name}-%{version}
%global ruby_abi     1.8-java

Name: torquebox-rubygem-activeresource-30
Version: 3.0.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
BuildArch: noarch
Summary: REST modeling framework (part of Rails)
URL: http://www.rubyonrails.org
Source0: http://rubygems.org/gems/activeresource-3.0.0.gem

Provides: %{tree_prefix}rubygem(%{gem_name}) = %{version}

Requires: ruby(abi) = %{ruby_abi}

Requires: %{tree_prefix}rubygem(activesupport) = 3.0.0
Requires: %{tree_prefix}rubygem(activemodel) = 3.0.0

%description

REST on Rails. Wrap your RESTful web app with Ruby classes and work with them like Active Record models.

%prep

%build

%install

rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{bin_dir}
install -m 755 -d %{buildroot}%{gem_dir}
install -m 755 -d %{buildroot}%{gem_dir}/gems/activeresource-3.0.0/lib
gem install --local --bindir %{buildroot}%{bin_dir} --install-dir %{buildroot}%{gem_dir} --force --ignore-dependencies --platform ruby %{SOURCE0}

%clean

rm -rf %{buildroot}

%files

%defattr(-, root, root, -)
%{bin_dir}/
%{gem_dir}/gems/activeresource-3.0.0/
%{gem_dir}/cache/activeresource-3.0.0.gem
%{gem_dir}/specifications/activeresource-3.0.0.gemspec
%doc %{gem_dir}/doc/activeresource-3.0.0

%changelog

