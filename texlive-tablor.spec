%global tl_name tablor
%global tl_revision 31855

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.07~g
Release:	%{tl_revision}.1
Summary:	Create tables of signs and of variations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tablor
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tablor.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tablor.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows the user to use the computer algebra system XCAS to
generate tables of signs and of variations (the actual plotting of the
tables uses the MetaPost macro package tableauVariations). Tables with
forbidden regions may be developed using the package. A configuration
file permits some configuration of the language to be used in the
diagrams. The tablor package requires that shell escape be enabled.

