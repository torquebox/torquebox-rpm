%global tree_prefix  torquebox-
%global ruby_sitelib /opt/jruby/lib/ruby/site_ruby/1.8
%global gem_dir      /opt/jruby/lib/ruby/gems/1.8
%global bin_dir      /opt/jruby/bin
%global gem_name     activemodel
%global gem_instdir  %{gem_dir}/gems/%{gem_name}-%{version}
%global ruby_abi     1.8-java

Name: torquebox-rubygem-activemodel-31
Version: 3.0.1
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
BuildArch: noarch
Summary: A toolkit for building modeling frameworks (part of Rails)
URL: http://www.rubyonrails.org
Source0: http://rubygems.org/gems/activemodel-3.0.1.gem

Provides: %{tree_prefix}rubygem(%{gem_name}) = %{version}

Requires: ruby(abi) = %{ruby_abi}

Requires: %{tree_prefix}rubygem(activesupport) = 3.0.1
Requires: %{tree_prefix}rubygem(builder) => 2.1.2
Requires: %{tree_prefix}rubygem(builder) < 2.2
Requires: %{tree_prefix}rubygem(i18n) => 0.4.1
Requires: %{tree_prefix}rubygem(i18n) < 0.5

%description

A toolkit for building modeling frameworks like Active Record and Active Resource. Rich support for attributes, callbacks, validations, observers, serialization, internationalization, and testing.

%prep

%build

%install

rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{bin_dir}
install -m 755 -d %{buildroot}%{gem_dir}
install -m 755 -d %{buildroot}%{gem_dir}/gems/activemodel-3.0.1/lib
gem install --local --bindir %{buildroot}%{bin_dir} --install-dir %{buildroot}%{gem_dir} --force --ignore-dependencies --platform ruby %{SOURCE0}

%clean

rm -rf %{buildroot}

%files

%defattr(-, root, root, -)
%{bin_dir}/
%{gem_dir}/gems/activemodel-3.0.1/
%{gem_dir}/cache/activemodel-3.0.1.gem
%{gem_dir}/specifications/activemodel-3.0.1.gemspec
%doc %{gem_dir}/doc/activemodel-3.0.1

%changelog

