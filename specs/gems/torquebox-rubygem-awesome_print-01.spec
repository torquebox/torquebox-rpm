%global tree_prefix  torquebox-
%global ruby_sitelib /opt/jruby/lib/ruby/site_ruby/1.8
%global gem_dir      /opt/jruby/lib/ruby/gems/1.8
%global bin_dir      /opt/jruby/bin
%global gem_name     awesome_print
%global gem_instdir  %{gem_dir}/gems/%{gem_name}-%{version}
%global ruby_abi     1.8-java

Name: torquebox-rubygem-awesome_print-01
Version: 0.2.1
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
BuildArch: noarch
Summary: Pretty print Ruby objects with proper indentation and colors
URL: http://github.com/michaeldv/awesome_print
Source0: http://rubygems.org/gems/awesome_print-0.2.1.gem

Provides: %{tree_prefix}rubygem(%{gem_name}) = %{version}

Requires: ruby(abi) = %{ruby_abi}


%description

Great Ruby dubugging companion: pretty print Ruby objects to visualize their structure. Supports Rails ActiveRecord objects via included mixin.

%prep

%build

%install

rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{bin_dir}
install -m 755 -d %{buildroot}%{gem_dir}
install -m 755 -d %{buildroot}%{gem_dir}/gems/awesome_print-0.2.1/lib
gem install --local --bindir %{buildroot}%{bin_dir} --install-dir %{buildroot}%{gem_dir} --force --ignore-dependencies --platform ruby %{SOURCE0}

%clean

rm -rf %{buildroot}

%files

%defattr(-, root, root, -)
%{bin_dir}/
%{gem_dir}/gems/awesome_print-0.2.1/
%{gem_dir}/cache/awesome_print-0.2.1.gem
%{gem_dir}/specifications/awesome_print-0.2.1.gemspec
%doc %{gem_dir}/doc/awesome_print-0.2.1

%changelog

